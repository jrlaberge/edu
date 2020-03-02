# Google Cloud Certified Professional Cloud Architect

This readme serves as my notes as I study for the Professional Cloud Architect certification exam

#### Table of Contents
Section 1: Linux Academy Course Notes
* [IAM](#iam)
* [Billing](#billing)
* [Monitoring with Stackdriver](#monitoring)


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

