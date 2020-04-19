# Google Cloud Certified Professional Cloud Architect

This readme serves as my notes as I study for the Professional Cloud Architect certification exam

### Table of Contents
#### Section 1: Linux Academy Course - Google Cloud Certified Professional Cloud Architect Course
* [IAM](#iam)
* [Billing](#billing)
* [Monitoring with Stackdriver](#monitoring)
* [Storage](#storage)
* [Managed Databases on GCP](#managed-databases)
* [Virtual Networks](#virtual-networks)
* [Practice Exam](#la-practice-exam)
#### Section 2: Additional Resources
* [Codelabs](#codelabs)
* [Google Cloud Solutions Architecture Reference](#gc-sa-reference)
* [GCP in 4 Words or Less](#gcp-4-words-or-less)
* [Official Google Cloud Blog](#gc-blog)
#### Section 3: Coursera Quizzes and Labs
* [Quizzes](#quizzes)
* [Labs](#labs)
* [Practice Exam](#coursera-practice-exam)
#### Section 4: GCP Products
[Google Cloud Products](#gcp-products)


# Section 1: Linux Academy Course - Google Cloud Certified Professional Cloud Architect Course

<a name="iam"/>

## IAM

IAM stands for Identity and Access Management.

Identity Access Management, is controlling who can access what. Best practice is to follow the principle of least privilege. This means, only assigning the bare minimum of access required. For example, instead of providing compute admin to a user/service account that is only accessing instances, instead, provide compute.instanceAdmin.

IAM falls under three pillars; 
1. (Member) Who = Member = Identity
2. (Role) Can do what = Role = Collection of permissions
3. (Resource) On which resource = Resource = What are we giving access to?

### Identity
* Google Account
* Service Account
* Google Group
* Google Apps Domain

### Role
* Primitive Role (Owner, Editor, Viewer)
* Predefined Role (compute.instanceAdmin, storage.objectAdmin,.. etc.)
* Custom Role (Combination of permissions to roll up into a specific role)

### Resource
Cloud Platform
Project
Compute Engine
...
etc.

Every user / service account requires an email. Email for users does not need to be a gmail/gsuite email.

Service accounts are used to allow access between applications and GCP services. It is much more benefical to user Service accounts as you can limit scope and access. 

Service accounts have keys managed by Google, however you can create your own key in either JSON (recommended) or P12 (for backwards compatibility).

Google recommends using the key managed by them if the service account is only used within Google Cloud, if it's used outside of Google Cloud, then use a user-generated key.

Also, as best practice recommends, you should rotate keys at regular intervals (Be careful when rotating keys, not to delete the key while it's in use as this could lead to downtime for your users)

<a name="billing"/>

## Billing

Billing uses billing accounts, a billing account can be assigned to multiple projects, but each project can only have one billing account.

Billing has the following roles/permissions:
* Billing Account Creator
    * Organization level only
    * Full access (create new billing accounts, add users etc.)
* Billing Account Administrator (Can do almost everything as Owner, such as link to projects
    * Configure billing export
    * Link/unlink projects
    * Manage billing user roles
* Billing Account User
    * Often paired with Project Creator
* Billing Account Viewer
    * Read-only, generally for finance
* Project Billing Manager
    * Similar to Billing Account User, but with no access to project resources.
    * Organization or project level

<a name="monitoring"/>

## Monitoring with Stackdriver

* Stackdriver is a suite of tools used for monitoring, logging, and tracking diagnostics for your applications.
* Google acquired Stackdriver -- Previously, it was exclusive to AWS
* Native monitoring of both GCP and AWS
    * Connect via service accounts/API's on other platforms/on-premises
* Dynamically discover all GCP resources
    * Install Stackdriver client on VMs for even greater levels of monitoring

### 6 Different Products
* Logging
    * Centralized logging
* Monitoring
    * Monitor metrics, health checks, dashboards and alerts
    * Exam Tip: Firewall rules must be enabled to allow source IPs of health checks (Can download source IP file)
* Error Reporting
    * Identify and understand app errors
* Trace
    * Find latency bottlenecks in applications
* Debug
    * Find/fix code errors in production
* Profiler (Beta)
    * Collect CPU/memory data - optimize performance

### Exam Perspective!
* IAM roles
* Exports
* How logging works with other Stackdriver products

### Concepts and Terminology
* Associated by project
    * Logs viewer only shows logs for one project
* Log entry -- records status or event
    * Includes log name (e.g. 'syslog', 'compute.googleapis.com/activity')
* Logs -- named collection of log entries
    * Only exist if there are log entries
* Retention period
    * Depends on log type

#### Pricing

* First 50GB per project, per month is free. $0.50/GB after that
* Admin and system event logs exempt
* Used to have tier system,(Standard and Premium) that has been replaced with usage only billing as of July 2018


#### Retention

Important to know the retention period of various logs.

| Log Type | Retention Period |
|----------|------------------|
| Admin Activity | 400 days |
| Data Access | 30 days |
| System Event | 400 days |
| Access Transparency | 400 days |
| All other logs | 30 days |

#### Exporting Logs

##### The basics:
* Requires a project and destination service
* Create filter -- select log entries to export
* Choose destination -- Cloud Storage, BigQuery, Pub/Sub
* Filter and destination held in a sink -- direct what entries to copy to which destination
* Only new entries will be exported after sink creation

#### IAM Roles
* Logging Admin - full control plus add others to logging iam
* Logs Viewer - view logs
* Logs Writer - Grant service accounts ability to write (create) logs
* Logs Configuration Writer - Create metrics and export sinks

### Monitoring
* Create uptime checks (ie. can use HTTP to probe an endpoint and view if it is available across multiple regions, and set alerts to notify when it's down)

### Trace, Debug, Error Reporting, and Profiler

#### Exam Perspective
* Conceptual knowledge on how each products is used to solve problems
* Interaction with Stackdriver Logging

#### Trace
* Find performance bottlenecks - lat ency (loading times)
* Collect data from Google App Engine (GAE), Google HTTP load balancers, or apps with Stackdriver Trace SDK
* Integrated into App Engine Standard - automatically enabled
* Available for GCE, GKE, and GAE (Flexible)
    * Requires enabling Stackdriver Trace API or SDK (depending on library)
* Can be installed on non-GCP resources

#### Trace answers/solves the following:
* How long does it take my application to handle a given request?
    * Why is it taking my application so long to handle a request?
    * Why do some of my requests take longer than others?
* What is the overall latency of requests to my application?
* Which microservice is calling a bottleneck?
* Has latency for my application increased or decreased over time?
* What can I do to reduce application latency?

#### Error Reporting
* Real-time error monitoring and alerting in your application
* Quickly understand errors
* Write to Stackdriver Logging or Error Reporting API (beta)
* Automatica and real-time analysis
    * Alerts and dashboards
* Built into App Engine Standard and Cloud Functions - automatically enabled
* In Beta for GAE Flexible, GCE, GKE, EC2 (AWS)
    * GCE, GKE, EC2 require Stackdriver logging agent to be installed
* Java, Python, JavaScript, Ruby, C#, PHP and Go

#### Debug
* Debug application
* Inspect appliccation state without stopping or slowing app
* Does not require adding log statements
* Automatically enabled in GAE Standard
* Available in GAE Flexible, GCE, and GKE with additional configuration
* Java, Python, Go, Node.js
* Can be installed on non-GCP resources

#### Profiler (beta)
* Profile resource intensive application components
* Collect CPU/RAM usage data -> associate with source code -> identify high resource usage components

<a name="storage" />

## Storage

### IAM Roles
* Below Roles can be set on a project, or bucket level:
   * Storage Admin
   * Storage Writer
   * Storage Viewer
* Storage Legacy Roles (Cannot be set project-wide):
   * Admin
   * Writer
   * Viewer
### ACL (Access Control Lists)
It is recommended to use IAM roles when possible, ACL rules allow you to configure specific ORW (Owner, Read, Writer) permissions on a bucket, or object level basis.


### Storage Bucket Types/Class

Regional / Multi-Regional (This cannot be changed once set, set on bucket)

* Multi-Regional 
   * Highest SLA, most expensive
* Regional
* Nearline
   * Good for data that may need to be accessed once per month
* Coldline
   * Good for data that *may* need to be accessed once per year, anything more than that, and Nearline usually works out to be a cheaper alternative.
   

### Object Versioning & Lifecycle Management


#### Versioning Terminology

* Generation
* Metageneration
* No realtionship between the two

#### Object Lifecycle Management

* Set Time To Live (TTL) on an object
   * Archive/Delete older verions
   * Downgrade storage classes
* Applied to bucket level
* Often paired to object versioning, but not required
* Examples:
   * Downgrade the storage class of objects older than X number of days
   * Delete objects created before X date
   * Keep only X amount of recent versions (versioning required to be enabled)
* Implemented with combination of Rules, Conditions, and Actions

##### Rules
##### Conditions
##### Action
* Delete

* SetStorageClass

#### Hands-On
In this lesson, we will go hands-on working with both object versioning and lifecycle management. Commands from the interactive diagram are listed below for further reference.

Check current versioning policy:

```
gsutil versioning get gs://&lt;BUCKET&gt;
```

Enable Object Versioning:

```
gsutil versioning set on gs://&lt;BUCKET&gt;
```

Check full object details in bucket:

```
gsutil ls -a gs://&lt;BUCKET&gt;
```

Download current lifecycle policy to local machine to edit:

```
gsutil lifecycle get gs://&lt;BUCKET&gt; > filename.json
```

Set new lifecycle policy after making above edits:

```
gsutil lifecycle set filename.json gs://&lt;BUCKET&gt;
```   

#### Gsutil Command-Line A-Z

Remove a bucket:

```
gsutil rm -r gs://<BUCKET>
```

Create a new bucket:

```
gsutil mb -l <location> -c <class> gs://<BUCKET>
```

Copy local files to bucket:
Note: Use -m for parallel threading


```
  gsutil -m cp -r <files/directory> gs://<BUCKET>
  ```
  
Check versioning policy:

```
gsutil versioning get gs://<BUCKET> 
```

Enable versioning:

```
gsutil versioning set on gs://<BUCKET>
```

View bucket folder contents:

```
gsutil ls gs://<BUCKET>/<folder>
```

View all subfolder contents:

```
gsutil ls -r gs://<BUCKET>
```

Change storage class in existing bucket:
Note: Disable versioning first


```
gsutil versioning set off gs://<BUCKET>
```

Note: Add -m for parallel threading


```
  gsutil -m rewrite -r -s NEARLINE gs://<BUCKET>/* 
  ```
  
Give public read access to an object via ACL:

```
gsutil acl ch -u AllUsers:R gs://<BUCKET/object>
```

Revoke public access:

```
gsutil acl ch -d AllUsers gs://<BUCKET/>object
```

Delete bucket:

```
gsutil rm -r gs://<BUCKET>
```

<a name="managed-databases" />

## Managed Databases on Google Cloud Platform

#### Database Options Include:
* Cloud SQL
* Cloud Spanner
* Cloud Storage for Firebase
* Cloud Storage
* Cloud Firestore for Firebase
* Cloud DataStore
* Cloud BigTable
* BigQuery

<dl>
   <dt> OLAP - Online Analytical Processing </dt>
   <dd> </dd>
   <dt> OLTP - Online Transactional Processing </dt>
   <dd> </dd>
   <dt> Relational Database Management System (RDBMS) </dt>
   <dd> Structured table (columns, and rows) </dd>
   <dt> Non Relational Database (NoSQL)</dt>
   <dd> Faster, commonly used in video games, mobile apps. Uses key:value pairs </dd>
</dl>

| |![cloud-sql](https://github.com/jrlaberge/edu/blob/master/cloud/google/img/Cloud_SQL.png?raw=true) <br> Cloud SQL | ![cloud-spanner](https://github.com/jrlaberge/edu/blob/master/cloud/google/img/Cloud_Spanner.png?raw=true) <br> Cloud Spanner | ![cloud-datastore](https://github.com/jrlaberge/edu/blob/master/cloud/google/img/Cloud_Datastore.png?raw=true) <br> Cloud Datastore (Firestore) | ![cloud-bigtable](https://github.com/jrlaberge/edu/blob/master/cloud/google/img/Cloud_Bigtable.png?raw=true) <br> Cloud Big Table |    ![bigquery](https://github.com/jrlaberge/edu/blob/master/cloud/google/img/BigQuery.png?raw=true) <br> BigQuery     |
|---|-----------|---------------|-----------------------------|-----------------|-----------------|
| | Relational|  Relational   |        Non-relational       | Non-relational  |  Data Warehouse | 
| Use Case | Structured Data Web Framework | RDBMS + scale, High Transactions | Semi-Structured Key-Value data | High throughput analytics | Mission critical apps, Scale + Consistency |
| Example | Medical records, Blogs | Global suplply chain, Retail | Product catalog, Game state | Graphs, IoT, Finance | Large data analytics Processing using SQL |

<a name="virtual-networks" />

## Virtual Networks

### Virtual Private Cloud (VPC)

#### The Basics

* A VPC is a software-defined network (SDN), a virtual version of traditional physical networks.
* VPCs are multi-regional by default
* A single VPC can contain many subnets (smaller segments of networks)
   * Subnets are regional (they can span multiple zones within a region)
* Project based, however can share between projects with Shared VPC
* Traditional networking concepts still apply. (ie. Firewall rules, Load Balancing, etc)
* Traffic to/from instances is controlled via Firewall rules
* VPC can contain both internal and external IP addresses
   * Internal (private addresses) range from: 10.0.0.0/8 (Class A), 172.16.0.0/12 (Class B), 192.168.0.0/16 (Class C)
* Incoming traffic (ingress) is free. Outgoing (egress traffic) has a cost.

IAM for VPC falls under compute engine. In order to access VPC on a new project, compute engine API will be enabled.
* Compute Admin (Full admin to instances and network)
* Compute Network Admin (Full network access only)

### Firewall

#### Basics

* Allow/deny traffic to and from instances
   * Based on configuration
* Manage both inbound (ingress) and outbound (egress) traffic
* Defined at network (VPC) level, but enforced for each instance
* Implied; deny all ingress traffic
* Implied; allow all egress traffic
* Firewall components:
   * Direction (ingress/egress)
   * Source
   * Target (destination)
   * Port / Protocol
   * Rule (Allow, Deny)
   * Priority (Order  rules evaluated - First matching rule is applied)

### Shared VPC

* Host project: Project that contains the Shared VPC
* Service project: Project that links to a shared VPC
* Standalone project: Project that does not use a shared VPC (default)
* Shared VPC admin: Admin for the shared VPC on host project
* Service project admin: Admin of shared VPC service project

#### Resources that can use shared VPC
* Compute Engine Instances
* Compute Engine Instance Templates
* Compute Engine Instance Groups
* Google Kubernetes Engine Clusters
* Internal IP Addresses
* Internal DNS
* Cloud DNS Private Zones
* Load Balancing


# Section 2: Additional Resources

<a name="codelabs" />

## Codelabs by Google

Visit [Codelabs](https://codelabs.developers.google.com/)
<a name="gc-sa-reference" />

## Google Cloud Solutions Architect Reference

Visit [gcp.solutions](https://gcp.solutions/)

<a name="gcp-4-words-or-less" />

## Google Cloud Platform in 4 Words or Less

Visit gregsramblings' [github](https://github.com/gregsramblings/google-cloud-4-words)

<a name="gc-blog" />

## Official Google Cloud Blog

Visit the [blog](https://cloud.google.com/blog/)


# Section 3: Coursera Quizzes and Labs

<a name="quizzes" />

## Quizzes

### Deploying Applications to Google Cloud
* You've been asked to write a program that uses Vision API to check for inappropriate content in  photos that are uploaded to a Cloud Storage bucket. Any photos that are inappropriate should be deleted. What might be the simplest, cheapest way to deploy in this program?
    * Cloud Functions, because the requirements for simplest and cheapest are met with Cloud Functions. Cloud Functions are for single  purpose functions like image analysis. Cloud Functions also can be  triggered by Cloud Storage events, so they provide seamless integration. The payment model based on number of request, processing time of request (measured in 100ms units), and then other resources consumed is the most suitable of all options offered above. There is a free tier too. Cloud Functions also provides automatic scaling, high availability, and fault tolerance.
* You have containerized multiple applications using Docker and have deployed them using Compute Engine VMs. You want to save cost and simplify container management. What might you do.
    * Migrate the containers to GKE, as the applications are containerized, and GKE will help with the resource efficiency and hence cost, automate many aspects of the container management, and provide the best solution for the scenario.
* You need to deploy an existing application that was written in .NET version 4.  The application requires Windows servers, and you don't want to change it. Which should you use?
    * Compute Engine is needed due to the Windows OS requirement.

### DevOps Automation
* What Google Cloud feature would be easiest to use to automate a build in response to code being checked into your source code repository?
    * Cloud Build triggers have been designed specifically to trigger a build automatically when changes are made to source code.
* Which Google Cloud tools can be used to build a continuous integration  pipeline?
    * Cloud Source Repositories, Cloud Build, Cloud Container Registry
* 

<a name="coursera-practice-exam" />

### Practice Exam - Coursera
* How to keep data in sync across regions? Which service should be used in the icon with the question mark in the diagram?
    * Cloud Storage
* An existing application uses websockets. To help migrate the application to cloud you should:
    * HTTP(S) load balancing natively supports websocket proxying.
* A company is building an image tagging pipeline. Which service should be used in the icon with the question mark in the diagram?
    * Cloud Pub/Sub
* How to store data to be accessed once a month and not needed after five years.
    * Nearline class, lifecycle policy to delete after 5 years.
* A company has a new IoT pipeline. Which services will make this design work?
    * Cloud IoT Core, Cloud Pub/Sub
* Multi-petabyte database for analysts that only know SQL and must be available 24 x 7.
    * BigQuery
* Which service completes the CI/CD pipeline? (Cloud Source -> ? -> Container Registry -> GCE -> GKE)
    * Cloud Container Builder
* Simply and reliably clone a Linux VM to another project in another region.
    * Snapshot the rood disk, create an image, and use the image for the new VM root disk.
* A company has this business requirement: ""Improve security by defining and adhering to a set of security and Identity and Access Management (IAM) best practices for cloud." Company security has locked out SSH access to production VMs. How can operations manage the VMs?
    * The operations team doesn't actually need SSH access to manage VMs. All it needs is Cloud Shell with the Cloud SDK and gcloud tools. Cloud Shell provides all the tools for managing Compute Engine instances. In this case the assumption that SSH access is needed is incorrect.
* What security strategy would you recommend for PII (Personally Identifiable Information) data on Cloud Storage?
    * No Cloud IAM roles to users, and granular ACLs on bucket
* A company has decided to use Cloud SDK tools to deploy to App Engine Flexible. Which one of the following requirements does this meet?
    * Use managed services whenever possible
* Which of the following business requirements can Cloud DNS help satisfy?
    * Cloud DNS records can be used to redirect customer traffic from on prem to cloud, thereby implementing the failover switch
* A company has business requirements to keep up with industry transformation and growth by adopting leading technology and to use "incremental innovation" based on business insights. Which one of the following Google Cloud Platform features will support this requirement?
    * BigQuery and Machine Learning are directly designed to be used to surface business insights from data. This is the best option.
* A game company wants to meet its scaling requirements and also provide insights to investors. Which solution will best meet these needs?
    * Stackdriver custom metrics can be crafted to expose specific game activities, which can be useful for autoscaling and provide a detailed source of indicators that may be relevant to investors.
* A company wants to test a risky update to an App Engine application requiring live traffic. Which of the following options is the best approach?
    * Deploying a new version, but not as default, is easily reversed. Traffic splitting enables testing with some live traffic, meeting the requirement.
* How to automatically and simultaneously deploy new code to each cluster?
    * Jenkins handles automation and simultaneous deployment.
* A microservice has intermittent problems that bursts logs. How can you trap it for live debugging?
    * A Stackdriver metric can identify a burst of log lines. You can set an alert. Then connect to the machine while the problem is happening.
* A company wants penetration security testing that primarily matches an end user perspective.
    * on prem scanners will approach from outside, and over the public internet is where the users are.
* A sales company runs weekly resiliency tests of the current build in a separate environment by replaying the last holiday sales load. What can improve resiliency?
    * Develop a script that mimics a zone outage and add it to the test.
* Release failures keep causing rollbacks in a web application. Fixes to QA process reduced rollbacks by 80%. What additional steps can you take?
    * Fragment the monolithic platform into microservices.
* A car reservation system has long-running transactions. Which one of the following deployment methods should be avoided?
    * Switching the load balancer from pointing at the green "good" environment to the blue "new" environment is a fast way to rollback if there is a problem during release. However, long-running transactions will be disrupted by that switch.
* Last week a region had a 1% failure rate in web tier VMs? How should you respond?
    * Perform RCA, reviewing cloud provider and deployment details to prevent simliar future failures.
* Why is it a recommended best practice not to assign blame to an individual or an organization?
    * Because it prematureley ends analysis, so you don't discover root cause in the technology or procedures
* A healthcare company wants to compliantly use Cloud Storage to store customer medical (HIPAA) data.
    * HIPAA is a complicated set of standards. Vendor certification is not sufficient. In general, many Google Cloud services are (can be) HIPAA compliant. However, before the service can be considered compliant, the client must execute a Business Associate Agreement (BAA) with Google. At that point, the service is compliant. But that does not mean the application that uses it is compliant. A third step is that the application and the processes must follow HIPAA standards
* Which network feature could help a company meet its global service expansion goals by reducing latency?
    * Cloud Content Delivery Network (CDN)
    

# Section 4: Google Cloud Products

<a name="gcp-products" />

## Google Cloud Products

### Content Delivery Network (CDN)

__Description:__ Google Cloud's CDN enables an organization to expand it's online presence with a single IP address and global reach leveraging Google's global network.

__Benefit:__ Reduces latency

