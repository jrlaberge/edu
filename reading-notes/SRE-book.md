## Site Reliability Engineering
[Site Reliability Engineering,](https://landing.google.com/sre/sre-book/toc/index.html) edited by Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (O'Reilly), Copyright 2016 Google Inc., 978-1-491-92912-4

#### Table of Contents
* [Chapter 6: Monitoring Distributed Systems](#monitoring)

<a href="monitoring" />

## Chapter 6: Monitoring Distributed Systems

### Key Terms
Monitoring
White-box monitoring
Black-box monitoring
Dashboard
Alert
Root Cause
Node and Machine
Push

#### Why Monitor?
Analyzing long-term trends
Comparing over time or experiment groups
Alerting
Building dashboards
Conducting ad hoc retrospective analysis (i.e., debugging)

### The Four Golden Signals
Latency
Traffic
Errors
Saturation

### Important Questions to Ask
Does this rule detect an otherwise undetected condition that is urgent, actionable and actively or imminently user-visible?
Will I ever be able to ignore this alert, knowing it's benign? When and why will I be able to ignore this alert, and how can I avoid this scenario?
Does this alert definitely indicate that users are being negatively affected? Are there detectable cases in which users aren't being negatively  impacted, such as drained traffic or test deployments, that should be filtered out?
Can I take action in response to this alert? Is that action urgent, or could it wait until morning? Could the action be safely automated? Will that action be a long-term fix, or just a short-term workaround?
Are other people getting paged for this issue, therefore rendering at least one of the pages unnecessary?

Every time the pager goes off, I should be able to react with a sense of urgency, I can only react with a sense of urgency a few times a day before I become fatigued.
Every page should be actionable.
Every page response should require intelligence. If a page merely merits a robotic response, it shouldn't be a page.
Pages should be about a novel problem or an event that hasn't been seen before.


