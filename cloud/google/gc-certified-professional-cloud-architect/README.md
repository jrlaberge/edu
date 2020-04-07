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
#### Section 2: Additional Resources
* [Codelabs](#codelabs)
* [Google Cloud Solutions Architecture Reference](#gc-sa-reference)
* [GCP in 4 Words or Less](#gcp-4-words-or-less)
* [Official Google Cloud Blog](#gc-blog)


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
