# IT Security

# Week 1

## Quiz

* You receive a legitimate-looking email from a sender that you recognize asking you to click a funny link. But, once you do, malware installs on your computer. What is most likely the reason you got infected?
    * The sender's email address was spoofed.
* If a hacker targets a vulnerable website by running commands that delete the website's data in its database, what type of attack did the hacker perform?
    * SQL Injection
* What type of attack can a hacker perform that involves injecting malicious code into a website to hijack a session cookie?
    * Cross-Site Scripting (XSS)
* What can occur during a ping of death (POD) attack? Check all that apply.
    * A Denial of Service (DOS)
    * A buffer Overflow
    * Remote code execution
* Which of these are ways a hacker can establish a man-in-the-middle attack? Check all that apply.
    * Rogue Access Point (Rogue AP)
    * An Evil Twin is a man-in-the middle attack where the victim connects to a network that is identical to a legit one, but is actually controlled by a hacker.
    * A common man-in-the-middle attack is “session hijacking” or “cookie hijacking.”
* An attacker, acting as a postal worker, used social engineering tactics to trick an employee into thinking she was legitimately delivering packages. The attacker was then able to gain physical access to a restricted area by following behind the employee into the building. What type of attack did the attacker perform? Check all that apply.
    * Social Engineering
    * Tailgating
* If a hacker can steal your passwords by installing malware that captures all the messages you type, what kind of malware did the hacker install? Check all that apply.
    * A Keylogger
    * Spyware
* Which of these is a characteristic of Trojan malware?
    * A trojan infection needs to be installed by the user
* What could potentially decrease the availability of security and also test the preparedness of data loss?
    * Ransomware
* Which of these is an example of the integrity principle that can ensure your data is accurate and untampered with?
    * Using Encapsulating Payload
    * Using MACs (Message Authentication Codes)
* What makes a DDOS different than a DOS attack?
    * DDOS is distributed (ie., Many sources)
    * DOS is singular (ie., One source)
* An attack that would allow someone to intercept your data as it's being sent or received is called a(n) _________ attack.
    * Man in the middle
* Botnets are designed to steal _____ from the victim.
    * Computing resources
* Phishing, baiting, and tailgating are examples of ________ attacks.
    * Social Engineering
* Which of these is true of vulnerabilities? Check all that apply.
    * A vulnerability is a flaw in the code of an application that can be exploited.
* What's the difference between a virus and a worm?
    * Viruses and worms are similar. The difference is that a virus spreads through files and worms don't need to attach to something to spread.
* Viruses and worms are similar. The difference is that a virus spreads through files and worms don't need to attach to something to spread.
    * Malware can use a victim's machine to perform a task controlled by a hacker. At that point, the compromised machine is known as a bot.

# Week 3

## Quiz

* Authn is short for ________.
    * Authentication
* The two types of one-time-password tokens are ______ and ______. Check all that apply.
    * An OTP generator token can be counter-based, where a counter is incremented on the token and the server upon successful authentication.
    * An OTP generator token can be time-based, staying in sync with the server using time.
* Security Keys utilize a secure challenge-and-response authentication system, which is based on ________.
    * Security keys use public key cryptography to perform a secure challenge response for authentication.
* Kerberos uses _____ as authentication tokens.
    * Kerberos issues tickets, which represent authentication and authorization tokens.
* Which of these passwords is the strongest for authenticating to a system?
    * P@w04d!$$L0N6 -- This is a strong password because of length, numbers, upper and lowercase letters, and special characters.
* A Lightweight Directory Access Protocol (LDAP) uses a _____ structure to hold directory objects.
    * Data Information Tree
* A network admin wants to use a Remote Authentication Dial-In User Service (RADIUS) protocol to allow 5 user accounts to connect company laptops to an access point in the office. These are generic users and will not be updated often. Which of these internal sources would be appropriate to store these accounts in?
    * A flat file is an internal source that can store user accounts on a RADIUS server.
* Kerberos enforces strict _____ requirements, otherwise authentication will fail.
    * Kerberos enforces strict time requirements, requiring the client and server clocks to be relatively closely synchronized, otherwise authentication will fail.
* In the three As of security, which part pertains to describing what the user account does or doesn't have access to?
    * Authorization pertains to describing what the user account does or doesn't have access to.
* A(n) _____ defines permissions or authorizations for objects.
    * An Access Control List (ACL) defines permissions or authorizations for objects.
* Access control entries can be created for what types of file system objects? Check all that apply.
    * Files
    * Folders
    * Programs
* Authz is short for ________.
    * Authorization
* In a Certificate Authority (CA) infrastructure, why is a client certificate used?
    * 
* A systems administrator is designing a directory architecture to support Linux servers using Lightweight Directory Access Protocol (LDAP). The directory needs to be able to make changes to directory objects securely. Which of these common operations supports these requirements?
    * 
* The authentication server is to authentication as the ticket granting service is to 
    * 
* Your bank set up multifactor authentication to access your account online. You know your password. What other factor combined with your password qualifies for multifactor authentication? Check all that apply.
    * Bank Card
    * Passphrase


## Creating a Company Culture for Security - Design Document

#### Overview: 
Now that you’re super knowledgeable about security, let's put your newfound know-how to the test. You may find yourself in a tech role someday, where you need to design and influence a culture of security within an organization. This project is your opportunity to practice these important skillsets.

#### Assignment: 
In this project, you’ll create a security infrastructure design document for a fictional organization. The security services and tools you describe in the document must be able to meet the needs of the organization. Your work will be evaluated according to how well you met the organization’s requirements.

#### About the organization: 
This fictional organization has a small, but growing, employee base, with 50 employees in one small office. The company is an online retailer of the world's finest artisanal, hand-crafted widgets. They've hired you on as a security consultant to help bring their operations into better shape.

#### Organization requirements: 
As the security consultant, the company needs you to add security measures to the following systems:

* An external website permitting users to browse and purchase widgets
* An internal intranet website for employees to use
* Secure remote access for engineering employees
* Reasonable, basic firewall rules
* Wireless coverage in the office
* Reasonably secure configurations for laptops

Since this is a retail company that will be handling customer payment data, the organization would like to be extra cautious about privacy. They don't want customer information falling into the hands of an attacker due to malware infections or lost devices.

Engineers will require access to internal websites, along with remote, command line access to their workstations.

What you'll do: You’ll create a security infrastructure design document for a fictional organization. Your plan needs to meet the organization's requirements and the following elements should be incorporated into your plan:

* Authentication system
* External website security
* Internal website security
* Remote access solution
* Firewall and basic rules recommendations
* Wireless security
* VLAN configuration recommendations
* Laptop security configuration
* Application policy recommendations
* Security and privacy policy recommendations
* Intrusion detection or prevention for systems containing customer data

### My security infrastructure design document

```
In order to secure our external website and our customer's data, we will need to implement security features to our website.

Customers can browse our products as a guest, but in order to purchase they will need to authenticate to our system by signing up for an account. We will implement captcha for sign up form and for login form as well.

HTTPS will be enforced, our site will use secure HTTP to ensure to our customers that we are who they think we are.

For internal website security, we will ensure proper monitoring and logging of our application. We will ensure that our code is designed to prevent XSS and SQL injections.

For our remote users that require access we will implement a VPN system to ensure they are able to access the intranet and related resources securely. For SSH, they will require on top of the VPN, RSA keys (public key cryptography).

Our firewall will be designed by utilizing a whitelist approach. We will by default deny/block all traffic. And then whitelist the services we need. For instance, we know we need https access which uses tcp port 443, or ssh which uses tcp port 22. 

For our wireless security, we will use WPA2 which uses strong encryption (AES), and have this on a different network segment than our wired connections to isolate them.

VLANs play an important part in our network, we can isolate various bits of traffic. We can have phones (VOIP) on one vlan, and user devices on another, and any internal systems on another as well.

Laptops will utilize Active Directory for centralized authentication and management of our users. We will also utilize centralized Endpoint protection to allow us to detect malware and other potential security threats as they happen.

Applications should be vetted prior to being installed, so we can have an application policy to block the installation of third-party apps that are not known/trusted by the IT department.

Security and privacy policy will outline how our data can and should be used. In order to help enforce this, we will have authentication systems in place where needed and monitoring, logging and auditing (accounting) of all actions taken on our systems. This can help us react quickly or discover security incidents.

By having firewalls both on the network and host-based, we can prevent many of the potential intrusions. In order to improve intrusion detection, we can also implement TACACS+.

Overall, security is a very important concept that needs to be thought about carefully. In a digital world, we have removed many boundaries that we once had, such as the ability to be on-demand for our users, scale nearly infinitely and hold and store immense amounts of data over the internet. This also poses security risks as there are individuals that would look to exploit any vulnerability they can find. So as IT folks, we must take security seriously and be vigilant. 
```

#### Sample Submission:
```
Authentication
Authentication will be handled centrally by an LDAP server and will incorporate One-Time Password generators as a 2nd factor for authentication.

External Website
The customer-facing website will be served via HTTPS, since it will be serving an e-commerce site permitting visitors to browse and purchase products, as well as create and log into accounts. This website would be publically accessible.

Internal Website
The internal employee website will also be served over HTTPS, as it will require authentication for employees to access. It will also only be accessible from the internal company network and only with an authenticated account.

Remote Access
Since engineers require remote access to internal websites, as well as remote command line access to workstations, a network-level VPN solution will be needed, like OpenVPN. To make internal website access easier, a reverse proxy is recommended, in addition to VPN. Both of these would rely on the LDAP server that was previously mentioned for authentication and authorization.

Firewall
A network-based firewall appliance would be required. It would include rules to permit traffic for various services, starting with an implicit deny rule, then selectively opening ports. Rules will also be needed to allow public access to the external website, and to permit traffic to the reverse proxy server and the VPN server.

Wireless
For wireless security, 802.1X with EAP-TLS should be used. This would require the use of client certificates, which can also be used to authenticate other services, like VPN, reverse proxy, and internal website authentication. 802.1X is more secure and more easily managed as the company grows, making it a better choice than WPA2.

VLANs
Incorporating VLANs into the network structure is recommended as a form of network segmentation; it will make controlling access to various services easier to manage. VLANs can be created for broad roles or functions for devices and services. An engineering VLAN can be used to place all engineering workstations and engineering services on. An Infrastructure VLAN can be used for all infrastructure devices, like wireless APs, network devices, and critical servers like authentication. A Sales VLAN can be used for non-engineering machines, and a Guest VLAN would be useful for other devices that don't fit the other VLAN assignments.

Laptop Security
As the company handles payment information and user data, privacy is a big concern. Laptops should have full disk encryption (FDE) as a requirement, to protect against unauthorized data access if a device is lost or stolen. Antivirus software is also strongly advised to avoid infections from common malware. To protect against more uncommon attacks and unknown threats, binary whitelisting software is recommended, in addition to antivirus software.

Application Policy
To further enhance the security of client machines, an application policy should be in place to restrict the installation of third-party software to only applications that are related to work functions. Specifically, risky and legally questionable application categories should be explicitly banned. This would include things like pirated software, license key generators, and cracked software.

In addition to policies that restrict some forms of software, a policy should also be included to require the timely installation of software patches. “Timely” in this case will be defined as 30 days from the wide availability of the patch.

User Data Privacy Policy
As the company takes user privacy very seriously, some strong policies around accessing user data are a critical requirement. User data must only be accessed for specific work purposes, related to a particular task or project. Requests must be made for specific pieces of data, rather than overly broad, exploratory requests. Requests must be reviewed and approved before access is granted. Only after review and approval will an individual be granted access to the specific user data requested. Access requests to user data should also have an end date.

In addition to accessing user data, policies regarding the handling and storage of user data are also important to have defined. These will help prevent user data from being lost and falling into the wrong hands. User data should not be permitted on portable storage devices, like USB keys or external hard drives. If an exception is necessary, an encrypted portable hard drive should be used to transport user data. User data at rest should always be contained on encrypted media to protect it from unauthorized access.

Security Policy
To ensure that strong and secure passwords are used, the password policy below should be enforced:

Password must have a minimum length of 8 characters
Password must include a minimum of one special character or punctuation
Password must be changed once every 12 months
In addition to these password requirements, a mandatory security training must be completed by every employee once every year. This should cover common security-related scenarios, like how to avoid falling victim to phishing attacks, good practices for keeping your laptop safe, and new threats that have emerged since the last time the course was taken.

Intrusion Detection or Prevention Systems
A Network Intrusion Detection System is recommended to watch network activity for signs of an attack or malware infection. This would allow for good monitoring capabilities without inconveniencing users of the network. A Network Intrusion Prevention System (NIPS) is recommended for the network where the servers containing user data are located; it contains much more valuable data, which is more likely to be targeted in an attack. In addition to Network Intrusion Prevention, Host-based Intrusion Detection (HIDS) software is also recommended to be installed on these servers to enhance monitoring of these important systems.
```

A great submission should include:

* Two authentication system requirements, like Security Key-based multifactor or OTP-based multifactor, and some kind of centralized authentication system (e.g., LDAP or Active Directory).
* A description of HTTPS.
* Recommendation for both a VPN service and a reverse proxy solution.
* A description of two or more types of firewall services (e.g., implicit deny rule, remote access, websites).
* Requirement for 802.1X.
* A description of four VLAN requirements, including Engineering VLAN, Sales VLAN, Infrastructure VLAN, and Guest VLAN.
* Three laptop security requirements, including FDE recommendations, antivirus recommendation, and a binary whitelisting recommendation.
* Requirement for a software update requirement policy and a requirement for restrictions on the types of applications permitted.
* Recommendations for rules protecting access to user data and for rules protecting the storage of user data.
* A description of four of the following security policy recommendations: passwords requiring a minimum of 8 characters; passwords requiring special characters; requiring periodic password changes > 6 months; and some form of mandatory security training for users.
* A requirement for a NIPS/NIDS on the network for customer data and a requirement for HIPS/HIDS on systems containing customer data.