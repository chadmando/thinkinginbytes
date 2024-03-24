+++
categories = [ "business" ]
title = "Better Business Email:Shared Inbox"
description = "Small businesses should keep process related emails out of personal mailboxes."
slug = "business-email-shared-inbox"
date = "202-03-23"
lastmod = "2024-03-23"
tags = [ "email", "process" ]
draft = true
+++

I plan to create a series of posts about how to do business email better.
By better, I mean less.
Less email sent, received, read, re-read, saved, and deleted.
Less long threads that morph and twist into one or more different topics.
Less critical business information trapped in a personal mailbox.

## TL;DR: Keep Business Process Email Out of Personal Mailboxes

Don't use personal mailboxes for business process email.
Its a mistake that creates the following problems:

* Others can't access when the user is sick or on vacation
* If the employee leaves the company, a serious effort is needed to reroute important mail.
* Business processes can't be built around a personal mailbox
* Adding new team members or transitioning new users into the role

For small businesses using a Microsoft 365 subscription, such as Microsoft 365 Business Standard or Microsoft 365 Business Premium, setting up a Shared Mailbox is easy for administrators.[^1] [^2]

## The Scenario

Here is a common scenario in a small business:

You run a small business.
Betty is the bookkeeper.
She enters vendor bill data into the accounts payable system.
Betty does quality work, is dependable, and takes pride in paying vendors on-time.
She checks all bills against open Purchase Orders and quickly resolves payment issues.
Her email is used as the "accounts payable" email address for all vendors. 
She is well-organized and separates the vendor emails into subfolders at the end of every week.


One day, while Betty is on vacation, a vendor informs you they are holding all future shipments until you pay an outstanding bill.
It appears that the vendor's email systems suffered an temporary outage and they assumed you received a bill that never left their servers!
The accounting system contains no outstanding balance for the vendor.
You ask them to re-send the bill, so you can enter and pay before any critical orders are delayed.
Several hours pass and no bill.
You call the vendor to confirm they have re-sent the bill.
They did.
It was sent to the email on file for accounts payable, Betty's.
You kindly request that the bill be sent to you.
After a few minutes, the bill arrives.
The bill is promptly entered and paid.
You send the vendor a photo of the check, mail it, and move on with your day.


Betty returns from vacation two days later.
She checks her email right away and sees the vendor's bill.
Based on the bill's due date, Betty is concerned because this means your company is past due.
She confirms that there is no unpaid bill with this reference number and enters it to be paid.
She even calls the vendor to confirm the bill is past due.
Because the check is _in the mail_, the vendor responds that no payment has been received.
Betty stops all work, enters the bill, and prints a check for payment.
She sets the check on your desk for signature.

Surprised that you are seeing another rush payment for this vendor, you ask her to explain the situation.
You realize that this is duplicate payment and tell Betty the story about the vendor call a few days ago.


What is the point of this story?
No harm done, right?
It isn't like you double-paid the bill and are now working to get a refund or applied to another bill.
The point of this story is that _valuable time_ was lost, and this could have easily been avoided.


Can you think of any other scenarios where having business process type email delivered to personal mailboxes would cause similar issues?

* Betty retires and tries to transition all vendors the her replacement's email address.
* Betty gets promoted and is asked to train her replacement.
* 

You can easy see another problematic situation, Betty retires and transitions someone new to her position.
What is the solution to avoid this situation.
It might be better to first look at the _non-solutions_ to this problem.

## Non-Solution: Can't You Just Give Others Access To Betty's Mailbox?

You could ask an administrator to give you access to Betty's mailbox.
This is a common solution to the problem of critical business information being trapped in a personal mailbox.
I don't recommend this, and neither should you.
In this scenario, it is likely that Betty may handle other matters in the business that may be sensitive.
She could handle HR issues or process special payrolls at the owners' request.
All of Betty's business responsibilities must be thoroughly reviewed before giving another employee Read Permission on her mailbox.
Depending on company policies, Betty may also need to be consulted before adding users to her mail.

## Non-Solution: Use Mail Rules To Forward Email While Out-Of-Office

The heading of this section should make any email administrator cringe.
A possible solution to others monitoring Betty's email is to forward messages from certain email addresses.
This can be done, but it creates a fragile fix.
You would need to collect a set of email domains to be forwarded.
This list  then needs to be reviewed in case any non-bill or sensitive information comes from that domain.
If the list isn't complete or subsequent filtering isn't expertly crafted, the results could be a mess.

## Solution: Setup a Shared Mailbox for Accounts Payable

Create a Shared Mailbox.
Add users that need access to the mailbox.
As needs change, add or remove users to suit.

* Allows others to view the current state of the email
* Creates an easy way to add or remove users
* Processes can be created and audited

There are challenges associated with managing a shared mailbox.

## Considerations For Managing A Shared Mailbox

1. Establish rules for working in the mailbox

* How To Handle Read or Unread Messages
Everyone using the shared mailbox should know how to handle Unread Message.
The risk of not setting up is confusion and mistakes.

* How to Handle completed messages Mark or move completed emails
Some action must be taken with when a message has been processed.
It could be deleting the message, moving to a folder, or marking it as _Completed_.
There should be no question that message in the Inbox are work in progress.

* How to identify messages that are waiting on resolution.
Flag Emails That Are In Progress.

Use the follow up flag to indicate that you are waiting on something from the sender.

* What to do with:
    Unread email
    read email
    email that you've completed work on


## References

[^1]: Microsoft Learn instructions for creating a shared mailbox
[^2]: Shared mailbox setup instructions from my Exchange PowerShell Recipes
