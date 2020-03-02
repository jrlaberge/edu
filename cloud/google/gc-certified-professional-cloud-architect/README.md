# Google Cloud Certified Professional Cloud Architect
======

This readme serves as my notes as I study for the Professional Cloud Architect certification exam

#### Table of Contents
Section 1: Linux Academy Course Notes
   [IAM](#iam)
   [Billing](#billing)

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

