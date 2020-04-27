# Interview Questions and Preparation


## Table of Contents
* [System Administrator](#sys-admin)


<a name="sys-admin" />

## System Administrator

* What is BGP?
  * BGP stands for Border Gateway Protocol. BGP is an important and essential part of the internet. It allows for fast and efficient routing of data over the internet. Similar to a postal service, where mail is sent to and it determines the best most efficient route to have that mail delivered. BGP is what allows data that spans the globe to be delivered quickly.
  * An important concept is Atonomous Systems (AS), these are smaller networks that make up the internet. BGP will hop from AS to AS to eventually reach it's destination.
  
* What is TCP and 3-Way Handshake?
  * TCP stands for Transmission Control Protocol, it is a connection oriented protocol, which means it provides accurate and reliable transmission of data. It accomplishes this using the 3-Way Handshake. Which starts by the client sending a SYN packet, and the server responding with a SYNACK (sync acknowledge), and the client sending a follow up ACK to inform the server that it was recieved.

* What is an IP address?

* What is a subnet mask?

* What is ARP?

* What is ARP Cache Poisoning?

* What is the ANDing process?

* What is a default gateway? What happens if I don't have one?

* Can a workstation computer be configured to browse the Internet and yet NOT have a default gateway?

* What is a subnet?

* What is APIPA?

* What is an RFC? Name a few if possible (not necessarily the numbers, just the ideas behind them)

* What is RFC 1918?

* What is CIDR?

* You have the following Network ID: 192.115.103.64/27. What is the IP range for your network?

* You have the following Network ID: 131.112.0.0. You need at least 500 hosts per network. How many networks can you create? What subnet mask will you use?

* You need to view at network traffic. What will you use? Name a few tools

* How do I know the path that a packet takes to the destination?

* What does the ping 192.168.0.1 -l 1000 -n 100 command do?

* What is DHCP? What are the benefits and drawbacks of using it?

* Describe the steps taken by the client and DHCP server in order to obtain an IP address.

* What is the DHCPNACK and when do I get one? Name 2 scenarios.

* What ports are used by DHCP and the DHCP clients?

* Describe the process of installing a DHCP server in an AD infrastructure.

* What is DHCPINFORM?

* Describe the integration between DHCP and DNS.

* What options in DHCP do you regularly use for an MS network?

* What are User Classes and Vendor Classes in DHCP?

* How do I configure a client machine to use a specific User Class?

* What is the BOOTP protocol used for, where might you find it in Windows network infrastructure?

* DNS zones - describe the differences between the 4 types.

* DNS record types - describe the most important ones.

* Describe the process of working with an external domain name

* Describe the importance of DNS to AD.

* Describe a few methods of finding an MX record for a remote domain on the Internet.

* What does "Disable Recursion" in DNS mean?

* What could cause the Forwarders and Root Hints to be grayed out?

* What is a "Single Label domain name" and what sort of issues can it cause?

* What is the "in-addr.arpa" zone used for?

* What are the requirements from DNS to support AD?

* How do you manually create SRV records in DNS?

* Name 3 benefits of using AD-integrated zones.

* What are the benefits of using Windows 2003 DNS when using AD-integrated zones?

* You installed a new AD domain and the new (and first) DC has not registered its SRV records in DNS. Name a few possible causes.

* What are the benefits and scenarios of using Stub zones?

* What are the benefits and scenarios of using Conditional Forwarding?

* What are the differences between Windows Clustering, Network Load Balancing and Round Robin, and scenarios for each use?

* How do I work with the Host Name Cache on a Client Computer?

* How do I clear the DNS cache on the DNS server?

* What is the 224.0.1.24 address used for?

* What is WINS and when do we use it?

* Can you have a Microsoft-based network without any WINS server on it? What are the "considerations" regarding not using WINS?

* Describe the differences between WINS push and pull replications.

* What is the difference between tombstoning a WINS record and simply deleting it?

* Name the NetBIOS names you might expect from a Windows 2003 DC that is registered in WINS.

* Describe the role of the Routing Table on a Host and on a Router.

* What are Routing Protocols? Why do we need them? Name a few.

* What are Router Interfaces? What types can they be?

* In Windows 2003 Routing, what are the interface filters?

* What is NAT?

* What is the real difference between NAT and PAT?

* How do you configure NAT on Windows 2003?

* How do you allow inbound traffic for specific hosts on Windows 2003 NAT?

* What is VPN? What types of VPN does Windows 2000 and beyond work with natively?

* What is IAS? In what scenarios do we use it?

* What's the difference between Mixed mode and Native mode in AD when dealing with RRAS?

* What is the "RAS and IAS" group in AD?

* What are Conditions and Profile in RRAS Policies?

* What types or authentication can a Windows 2003 based RRAS work with?

* How does SSL work?

* How does IPSec work?

* How do I deploy IPSec for a large number of computers?

* What types of authentication can IPSec use?

* What is PFS (Perfect Forward Secrecy) in IPSec?

* How do I monitor IPSec?

* Looking at IPSec-encrypted traffic with a sniffer. What packet types do I see?

* What can you do with NETSH?

* How do I look at the open ports on my machine?

* What is Active Directory?

* What is LDAP?

* Can you connect Active Directory to other 3rd-party Directory Services? Name a few options.

* Where is the AD database held? What other folders are related to AD?

* What is the SYSVOL folder?

* Name the AD NCs and replication issues for each NC.

* What are application partitions? When do I use them?

* How do you create a new application partition?

* How do you view replication properties for AD partitions and DCs?

* What is the Global Catalog?

* How do you view all the GCs in the forest?

* Why not make all DCs in a large forest as GCs?

* Trying to look at the Schema, how can I do that?

* What are the Support Tools? Why do I need them?

* What is LDP? What is REPLMON? What is ADSIEDIT? What is NETDOM? What is REPADMIN?

* What are sites? What are they used for?

* What's the difference between a site link's schedule and interval?

* What is the KCC?

* What is the ISTG? Who has that role by default?

* What are the requirements for installing AD on a new server?

* What can you do to promote a server to DC if you're in a remote location with slow WAN link?

* How can you forcibly remove AD from a server, and what do you do later? o Can I get user passwords from the AD database?

* What tool would I use to try to grab security related packets from the wire?

* Name some OU Design Considerations.

* What is tombstone lifetime attribute?

* What do you do to install a new Windows 2003 DC in a Windows 2000 AD?

* What do you do to install a new Windows 2003 R2 DC in a Windows 2003 AD?

* How would you find all users that have not logged on since last month?

* What are the DS* commands?

* What's the difference between LDIFDE and CSVDE? Usage considerations?

* What are the FSMO roles? Who has them by default? What happens when each one fails?

* What FSMO placement considerations do you know of?

* I want to look at the RID allocation table for a DC. What do I do?

* What's the difference between transferring a FSMO role and seizing one? Which one should you NOT seize?Why?

* How do you configure a "stand-by operation master" for any of the roles?

* How do you backup AD?

* How do you restore AD?

* How do you change the DS Restore admin password?

* Why can't you restore a DC that was backed up 4 months ago?

* What are GPOs?

* What is the order in which GPOs are applied?

* Name a few benefits of using GPMC.

* What are the GPC and the GPT? Where can I find them?

* What are GPO links? What special things can I do to them?

* What can I do to prevent inheritance from above?

* How can I override blocking of inheritance?

* How can you determine what GPO was and was not applied for a user? Name a few ways to do that.

* A user claims he did not receive a GPO, yet his user and computer accounts are in the right OU, and everyone else there gets the GPO. What will you look for?

* Name a few differences in Vista GPOs.

* Name some GPO settings in the computer and user parts.

* What are Administrative Templates?

* What's the difference between Software Publishing and Assigning?

* Can I deploy non-MSI software with GPO?

* You want to Standardize the Desktop Environments (wallpaper, My Documents, Start menu, printers etc.) on the computers in one department. How would you do that?

* Tell me a bit about the Capabilities of Exchange Server.

* What are the different Exchange 2003 versions?

* What's the main differences between Exchange 5.5 and Exchange 2000/2003?

* What are the major network infrastructure for installing Exchange 2003?

* What is the latest Exchange 2003 Service Pack? Name a few changes in functionality in that SP.

* What are the disk considerations when installing Exchange (RAID types, locations and so on).

* You got a new HP DL380 (2U) server, dual Xeon, 4GB of RAM, 7 SAS disks, 64-bit. What do you do next to install Exchange 2003? (you have AD in place)

* Why not install Exchange on the same machine as a DC?

* How would you prepare the AD Schema in advance before installing Exchange?

* What type or permissions do you need in order to install the first Exchange Server in a forest? And in a domain?

* How would you verify that the Schema was actually updated?

* What type of memory optimization changes could you do for Exchange 2003?

* How would you check your Exchange configuration settings to see if they're right?

* What are the Exchange management tools? How and where can you install them?

* What types of permissions are configurable for Exchange?

* How can you grant access for an administrator to access all mailboxes on a specific server?

* What is the Send As permission?

* What other management tools are used to manage and control Exchange 2003? Name the tools you'd use.

* What are Exchange Recipient types? Name 5.

* You created a mailbox for a user, yet the mailbox does not appear in ESM. Why?

* You wanted to change mailbox access permissions for a mailbox, yet you see the SELF permission alone on the permissions list. Why?

* What are Query Based Distribution groups?

* What type of groups would you use when configuring distribution groups in a multiple domain forest?

* Name a few configuration options for Exchange recipients.

* What's the difference between Exchange 2003 Std. and Ent. editions when related to storage options and size?

* Name a few configuration options related to mailbox stores.

* What are System Public Folders? Where would you find them?

* How would you plan and configure Public Folder redundancy?

* How can you immediately stop PF replication?

* How can you prevent PF referral across slow WAN links?

* What types of PF management tools might you use?

* What are the differences between Administrative Permissions and Client Permissions in PF?

* How can you configure PF replication from the command prompt in Exchange 2003?

* What are the message hygiene options you can use natively in Exchange 2003?

* What are the configuration options in IMF?

* What are virtual servers? When would you use more than one?

* Name some of the SMTP Virtual Server configuration options.

* What is a Mail Relay? Name a few known mail relay software or hardware options.

* What is a Smart Host? Where would you configure it?

* What are Routing Groups? When would you use them?

* What are the types of Connectors you can use in Exchange?

* What is the cost option in Exchange connectors?

* What is the Link State Table? How would you view it?

* How would you configure mail transfer security between 2 routing groups?

* What is the Routing Group Master? Who holds that role?

* Explain the configuration steps required to allow Exchange 2003 to send and receive email from the Internet (consider a one-site multiple server scenario).

* What is DS2MB?

* What is Forms Based Authentication?

* How would you configure OWA's settings on an Exchange server?

* What is DSACCESS?

* What are Recipient Policies?

* How would you work with Multiple Recipient Policies?

* What is the "issue" with trying to remove email addresses added by recipient policies? How would you fix that?

* What is the RUS?

* When would you need to manually create additional RUS?

* What are Address Lists?

* How would you modify the filter properties of one of the default address lists?

* How can you create multiple GALs and allow the users to only see the one related to them?

* What is a Front End server? In what scenarios would you use one?

* What type of authentication is used on the front end servers?

* When would you use NLB?

* How would you achieve incoming mail redundancy?

* What are the 4 types of Exchange backups?

* What is the Dial-Tone server scenario?

* When would you use offline backup?

* How do you re-install Exchange on a server that has crashed but with AD intact?

* What is the Dumpster?

* What are the e00xxxxx.log files?

* What is the e00.chk file?

* What is Circular Logging? When would you use it?

* What's the difference between Online and Offline defrag?

* How would you know if it is time to perform an offline defrag of your Exchange stores?

* How would you plan for, and perform the offline defrag?

* What is the eseutil command?

* What is the isinteg command?

* How would you monitor Exchange's services and performance? Name 2 or 3 options.

* Name all the client connection options in Exchange 2003.

* What is Direct Push? What are the requirements to run it?

* How would you remote wipe a PPC?

* What are the issues with connecting Outlook from a remote computer to your mailbox?

* How would you solve those issues? Name 2 or 3 methods

* What is RPC over HTTP? What are the requirements to run it?

* What is Cached Mode in OL2003/2007?

* What are the benefits and "issues" when using cached mode? How would you tackle those issues?

* What is S/MIME? What are the usage scenarios for S/MIME?

* What are the IPSec usage scenarios for Exchange 2003?

* How do you enable SSL on OWA?

* What are the considerations for obtaining a digital certificate for SSL on Exchange?

* Name a few 3rd-party CAs.

* What do you need to consider when using a client-type AV software on an Exchange server?

* What are the different clustering options in Exchange 2003? Which one would you choose and why.

* What is FSB?

* What are Vcore and Vi/o?

* On what type of socket can you install a Pentium 4 CPU?

* What is SMP?

* Which Intel and AMD processors support SMP?

* How do LGA sockets differ from PGA and SEC?

* What is the difference between Pentium 4 and Pentium Core 2 Duo? Explain the new technology.

* How does IRQ priority works?

* What technology enables you to upgrade your computer's BIOS by simply using a software?

* What happens if you dissemble the battery located on the Mother-Board?

* How do L1, L2, and L3 work?

* How should we install RAM on a Dual-Channel Motherboard?
