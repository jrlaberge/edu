import os
import re

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
# Remove API KEY!!!
os.environ["API_KEY"] = 'pk_f5d7932e01a742d1a2d23325c09f24b0'
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():

    """Show portfolio of stocks"""
    # Unique stocks purchased
    username = session["username"]
    user_id = session["user_id"]
    users_stocks = db.execute("SELECT DISTINCT symbol FROM stocks as s, transactions as t WHERE t.stock_id = s.id AND t.user_id = :user_id and t.action = 'BUY'", user_id = user_id)
    users_cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id = user_id)[0]['cash']
    users_total_balance = users_cash

    if not users_stocks:
        return render_template("index.html",  username = username, cash = usd(users_cash))
    else:
        users_portfolio = []
        for symbol in users_stocks:
            symbol = symbol["symbol"]
            stock_info = {}
            shares = db.execute("SELECT SUM(quantity) as shares FROM transactions WHERE user_id = :user_id AND stock_id = (SELECT id FROM stocks WHERE symbol = :symbol)", user_id = user_id, symbol = symbol)[0]['shares']
            if shares == 0:
                continue
            response = lookup(symbol)

            # Compile necessary information int a dict
            stock_info["symbol"] = symbol
            stock_info["name"] = response["name"]
            stock_info["price"] = response["price"]
            stock_info["shares"] = shares
            stock_info["total"] = response["price"] * stock_info["shares"]
            users_total_balance += stock_info["total"]

            # reformat for USD
            stock_info["price"] = usd(stock_info["price"])
            stock_info["total"] = usd(stock_info["total"])

            # add this dict to the users portfolio
            users_portfolio.append(stock_info)

        return render_template("index.html", username = username, users_portfolio = users_portfolio, cash = usd(users_cash), total = usd(users_total_balance))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == 'GET':
        return render_template("buy.html")
    else:
        qty = int(request.form.get("shares"))
        symbol = request.form.get("symbol")

        if qty < 1:
            return apology("You can only purchase a positive amount of shares")
        elif not symbol or not qty:
            return apology("You must enter a valid Symbol / Quantity")

        # Perform API call to lookup cost of shares
        response = lookup(symbol)
        symbol = response['symbol']
        price = response['price']
        name = response['name']

        total_price = qty * price

        # check if stock / symbol already exists
        stock_exists = db.execute('SELECT * FROM stocks WHERE symbol = :symbol', symbol=symbol)
        if not stock_exists:
            # insert stock into db
            db.execute('INSERT INTO stocks (symbol, company_name) VALUES (:symbol, :company_name)', symbol=symbol, company_name=name)

        # get available funds of user

        cash = db.execute('SELECT cash FROM USERS where username = :username', username=session['username'])[0]['cash']

        if cash < total_price:
            return apology("Not enough funds haha!")
        else:
            new_balance = cash - total_price
            try:
                db.execute('INSERT INTO transactions (user_id, stock_id, price, quantity, action) SELECT :user_id, id, :price, :quantity, :action FROM stocks WHERE symbol = :symbol',
                    user_id = session['user_id'],
                    price = price,
                    quantity = qty,
                    action = 'BUY',
                    symbol = symbol
                    )
            except Exception as e:
                print(e)
                return apology("Something went wrong.")

            # deduct cash from users balance
            try:
                db.execute("UPDATE users SET cash = :new_balance WHERE id = :user_id", new_balance = new_balance, user_id = session['user_id'])
            except Exception as e:
                print(e)
                return apology("Something went wrong")

            flash(u'Sucessfully purchased stocks.', 'primary')
            return redirect('/')





@app.route("/history")
@login_required
def history():
    transactions = db.execute('SELECT s.symbol, t.quantity, t.price, t.created_at, t.action from transactions as t, stocks as s where s.id = t.stock_id and t.user_id = :user_id order by created_at', user_id = session["user_id"])
    i = 0
    while i < len(transactions):
        transactions[i]['price'] = usd(transactions[i]['price'])

        i += 1
    return render_template('history.html', transactions = transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id, but maintain flashed message if present
    if session.get("_flashes"):
        flashes = session.get("_flashes")
        session.clear()
        session["_flashes"] = flashes
    else:
        session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash(u'invalid username and/or password', 'danger')
            return redirect('/login')

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == 'GET':
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        lookup_response = lookup(symbol)

        if not lookup_response:
            return apology("Stock not found.")

        share = lookup_response["name"]
        quote = usd(lookup_response["price"])

        return render_template("quote.html", share=share, symbol=symbol, quote=quote)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmation")

        if not username:
            return apology("Username must be provided!")
        elif db.execute("SELECT * FROM users WHERE username = :username", username=username):
            return apology("Username already exists.")

        if not password or not confirm_password:
            return apology("Both password fields are required.")
        elif password != confirm_password:
            return apology("Passwords do not match.")
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hashed_password)", username=username, hashed_password=generate_password_hash(password))

            flash(u'You have been registered successfully. Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            print(e)
            return apology("Something went wrong. :(")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == 'GET':
        return render_template('sell.html')
    else:
        symbol = request.form.get('symbol')
        shares_to_sell = int(request.form.get('shares'))

        if not shares_to_sell or not symbol:
            return apology("Symbol / Shares cannot be left blank")
        elif shares_to_sell < 1:
            return apology("Shares must be a positive integer, greater than 0")

        current_share_qty = db.execute('SELECT SUM(quantity) as qty FROM transactions')[0]['qty']

        if not current_share_qty or current_share_qty < shares_to_sell:
            return apology("It doesn't appear that you have enough of those stocks to sell.")

        try:
            # convert price into a negative integer to insert into db
            price = lookup(symbol)['price']
            shares_to_sell *= -1
            db.execute('INSERT INTO transactions (user_id, stock_id, price, quantity, action) SELECT :user_id, id, :price, :quantity, :action FROM stocks WHERE symbol = :symbol',
                    user_id = session['user_id'],
                    price = price,
                    quantity = shares_to_sell,
                    action = 'SELL',
                    symbol = symbol
                    )
        except Exception as e:
            return apology("Something went wrong.")

        flash(u'Sucessfully sold stocks.', 'primary')
        return redirect('/')

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    if request.method == 'GET':
        return render_template("account.html", username = session['username'])
    else:
        current_pw = request.form.get('current_password')
        new_pw = request.form.get('password')
        is_valid = password_checker(new_pw)

        users_pw = db.execute('SELECT hash FROM users where id = :user_id', user_id = session['user_id'])[0]['hash']

        if not check_password_hash(users_pw, current_pw):
            flash(u'The current password you have entered is incorrect.', 'danger')

        elif check_password_hash(users_pw, new_pw):
            flash(u'New password cannot be the same as your current/previous password.', 'warning')

        elif new_pw != request.form.get('confirmation'):
            flash(u'Passwords do not match', 'danger')

        elif not is_valid:
            flash(u'Password does not meet complexity requirements', 'danger')
            flash(u'Password should be at least 8 characters. Contain at least 1 of each (lower case, upper case, number, special character (?, #, $, ! etc.)', 'danger')

        else:
            hashed_pw = generate_password_hash(new_pw)
            try:
                db.execute('UPDATE users SET hash = :hashed_pw WHERE id = :user_id', hashed_pw = hashed_pw, user_id = session['user_id'])
                flash(u'Password has been changed successfully.', 'success')
            except Exception as e:
                print(e)
                flash (u'Something went wrong.', 'danger')

        return render_template("account.html", username = session['username'])



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

def password_checker(password):
    password_checks = {}
    password_checks['min_len'] = len(password) >= 8
    password_checks['has_upper'] = re.search('[A-Z]', password)
    password_checks['has_lower'] = re.search('[a-z]', password)
    password_checks['has_num'] = re.search('[0-9]', password)
    password_checks['has_nonAlpha'] = re.search('[^a-zA-Z\d\s:]', password)

    if False in password_checks.values() or None in password_checks.values():
        return False
    else:
        return True
