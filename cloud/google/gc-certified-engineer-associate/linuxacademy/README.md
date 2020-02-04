# Linux Academy Course
## Google Cloud Certified Associate Cloud Engineer

### Project: Find Seller Cloud Engineer

### Description: 

In this scenario, you’ve been hired by a startup called Find Seller. They're working on an app that allows users to post a picture of an item and tag it as something they want to buy or sell. They’re having trouble getting funded because currently all of their technology resides on the developers' laptops, and they don’t have any idea how to move to the cloud. That’s where you and I enter the scenario. You’ve been hired as a junior cloud operations engineer, and I’ll be working as a senior cloud engineer. I’ll be mentoring you as we’re assigned tasks from our boss, and we’ll go through the process of deploying and maintaining the application.

Here are some of the areas of focus:

- Set up a cloud solution environment.
- Plan and configure a cloud solution.
- Deploy and implement a cloud solution.
- Ensure successful operation of a cloud solution.
- Configure access and security.

By the end of this course, you should be ready to pass the Google Cloud Certified- Associate Cloud Engineer Exam

# Timeline
| Section | Start Date | Expected Complete Date | Actual Complete Date |
|:-------:|:----------:|:----------------------:|:--------------------:|
| 1.1     | 09/12/19   |09/12/19                |09/12/1               |

# Notes

# Section 1. Setting Up a Cloud Solution Environment

## 1.1 Setting up Cloud Projects and Accounts

#### Initial Tasks
1. Create Account
1. Create Project
1. Create IAM User for John with ML Developer Role
1. Enable ML API
1. Setup Stackdriver Account
1. Link G Suite Identities to Users
1. Create Billing Account
1. Setup Budget and Alerts
1. Install Cloud SDK
1. Create Google Cloud Presentation

### Creating an Account
Create account in console.cloud.google.com, this will be an Individual account as I am using GMail. It would be a business account if I was using a G Suite or Cloud Identity login.

### Creating a New Project
Create a project named find-seller-app-dev

### Creating Users and Assigning Roles
Create a user John, and grant access to ML Dev role

### Enable API
Go API -> Library and Enable Cloud Machine Learning Engine

### Provision Stackdriver Account
By navigating to Stackdriver / Monitoring section you can create a stackdriver account. You need to specify a host project, and this single account can monitor multiple projects / resources. 

#### Best Practice: 
If you are only monitoring a single project; then you can use the same project to host stackdriver.
If there are multiple projects, create a separate project that is empty and specifically for Stackdriver.

## 1.2 Managing Billing Configuration

### Creating Billing Accounts
Create a billing account for dev and prod

### Establishing Billing Budgets and Alerts
Create a billing budget of 500$ for dev

### Setting up Billing Exports to Estimate Daily/Monthly Charges
Billing export to google cloud storage bucket; exported as JSON with prefix dev-app-

Another option that provides more data would be exporting to BigQuery

### Billing Recap

Billing can be invoiced (monthly) or self-serve; invoiced requires going through Google Cloud Sales

Roles; Predefined;
- Billing Admin:  Generally CTO
- Billing User:   Users that will be creating billable projects
- Billing Viewer: Finance team


## 1.3 Cloud SDK

### Installing Cloud SDK
Following the instructions here: https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu to install Cloud SDK in my Ubuntu@WSL

`gcloud init` is required to get the SDK configured (initialized) and it will prompt you to login via web browser to authenticate yourself.

### Using the Cloud SDK

```Cloud SDK
\-- Components
    \-- gcloud
     |  \-- alpha
     |   \-- beta
     |
     \-- BQ
     \-- GSUtil
     \-- Core
```
Command structure `gcloud <group> <command>`

# 2 Planning and Configuring a Cloud Solution

## 2.1 Planning and Configuring Compute Resources

### Comparing Compute Options
App Engine, used to develop highly scalable web apps
Cloud Functions, Run Javascript code in response to cloud events
Kubernetes Engine, Deploy and Manage containerized applications (Only supports Docker)
Compute Engine, Can run anything/everything you would run in a VM


### Compute Engine, Managed Instances
Managed Instances, grouping of instances, great for autoscaling, can autoscale off various metrics and supports templates
Unmanaged Instances; can be used to load balance, doesn't support autoscaling.

### Kubernetes [K8S] Engine
![alt-text][k8s]

Controllers:
- Deployment.yaml (Desired State Config)
    - Ensures X amount of containers are running
- DaemonSet.yaml
    - Node Management
- Many more, 

Steps taken in this lesson:
1. Create a kubernetes cluster
    - Use Google's custom container OS COS
    - Default values; 3 nodes, enable stackdriver, enable auto-repair/upgrade, Zonal (cheaper option, regional would be better for HA)
2. Create a deployment.yaml (workload) to deploy Nginx to the cluster
3. Create a service; open port 80 and use a load balancer to provide a single external IP that will interally distribute to the nginx nodes in the pod.
4. Look at config map, this is for separating config from code. For instance you can specify which storage bucket to use etc.

### Comparing Storage Options

- Cloud Storage
    - Object Storage
- BigTable
    - NoSQL database for analytical workloads
- Cloud Spanner
    - Horizontally scalable, relational database service (RDBS)
- Cloud DataStore
    - NoSQL database suitable for web/mobile
- CloudSQL
    - Fully managed DB, supports MySQL (1st / 2nd Gen) and PostgreSQL
    
# 3

# 4 Ensuring Successful Operation of a Cloud Solution

## Managing Compute Instances

### SSH
We can create instances in the UI, and create firewall rules to open port 22/tcp to allow SSH traffic.

We can also ssh using the SDK by using the command: `gcloud compute ssh instance <user>@<instance-name>`

### Images and Snapshots

```
gcloud compute snapshots list
gcloud compute disks list
gcloud compute disks snapshot <disk-name>
```

```When using multiple projects, especially when they use different defaults, the Cloud SDK could become a pain point. However, it doesn't have to!

The Cloud SDK supports multiple configurations and allows us to activate the one we want to use easily.

Since there are a lot of different commands that we covered in this lesson, they are also listed below for cross reference:

Create a new gcloud configuration

gcloud config configurations create (CONFIG_NAME)

(Note that creating a configuration will automatically activate it as well)

List all of your gcloud configurations

gcloud config configurations list

Activate another existing gcloud configuration

gcloud config configurations activate (CONFIG_NAME)

List the settings for your active configuration

gcloud config list

Assign a project to a configuration

gcloud config set project (PROJECT_ID)

Set account for your configuration

gcloud config set account (ACCOUNT_ID)```
## References

[comment]: Image URLs
[k8s]: https://cloud.google.com/images/products/artwork/certified-kubernetes-color.svg
