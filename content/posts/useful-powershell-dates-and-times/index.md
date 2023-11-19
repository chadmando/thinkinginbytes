+++
categories = [ "technology" ]
title = "Useful PowerShell: Dates and Times"
description = "Use PowerShell For Date Calculations"
slug = "powershell-dates-times"
date = "2023-11-19T17:42:13.806Z"
tags = [ "powershell", "date", "time" ]
draft = false
+++
In this article:

<!-- TOC -->

- [What is PowerShell?](#what-is-powershell)
- [Finding And Opening The PowerShell Application](#finding-and-opening-the-powershell-application)
- [Creating A Date](#creating-a-date)
- [Creating A Specific Date](#creating-a-specific-date)
- [Something Useful: Finding Completion Dates](#something-useful-finding-completion-dates)
- [What About Weeks?](#what-about-weeks)
- [Find The Time Between Dates](#find-the-time-between-dates)
- [Conclusion](#conclusion)
- [References](#references)

<!-- /TOC -->

PowerShell provides immediate value for non-technical users.This article introduces new users to one useful feature of PowerShell without explaining the background of PowerShell and all the details behind cmdlets, objects, properties, variables, operators, members, help, execution policy, etc.
This is a different way of introducing PowerShell. Many introductions to PowerShell tackle the implementation details that, in my opinion, can be hidden from some users who just need a tool.

## What is PowerShell?

PowerShell is an application on your computer.
That is the level of detail required for this article.

Microsoft's answer to the question "What is PowerShell?":

>PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework. PowerShell runs on Windows, Linux, and macOS.

For more details on Microsoft's definition, consult the Microsoft PowerShell Docs [^1].

## Finding And Opening The PowerShell Application

All currently supported versions of Windows come with PowerShell installed. 
Some businesses hide or restrict access to PowerShell on their computers.
If you are using a work computer, you may have limited access to PowerShell.
If you do have access to PowerShell, its use may be restricted.

### PowerShell Versions

In a Windows environment, you may see three (3) different PowerShell applications.

+ Windows PowerShell
+ Windows PowerShell ISE
+ PowerShell

For this article, any of these will work.
The application may look different, but the functionality is the same.

{{< video src="launch_powershell_2.mp4" type="video/mp4" preload="auto" >}}

## Creating A Date

Create a date by typing `Get-Date`[^2] and then pressing `Enter`.
The value of the _date_ equals the moment the `Enter` key was pressed.

```pwsh
Get-Date
```

Results will vary depending on _when_ you are.
It'll look something like this:

```text
Saturday, October 28, 2023 11:37:36 AM
```

> Note: When typing `Get-Date`, PowerShell doesn't care about proper capitalization.
>`Get-Date`, `get-date`, `gEt-DAte`, all produce the same result.
> PowerShell is as *case-insensitive* as possible with a few exceptions[^3].

{{< video src="powershell_get-date.mp4" type="video/mp4" preload="auto" >}}

## Creating A Specific Date

To do useful things with dates in PowerShell, you'll need to create a date that is something other than *today*.
Create a specific date by adding a date after the `Get-Date` in the form of Month/Day/Year.

```pwsh
Get-Date 07/04/1776
```
To include the time of day in the date, add the hour and minute after the date.
By enclosing both the date and the time in double quotes, PowerShell knows they're connected.

```pwsh
Get-Date "07/04/1776 09:32"
```

{{< video src="powershell_getdate_specific.mp4" type="video/mp4" preload="auto" >}}

Without the quotation marks, PowerShell returns an error message.

```text
Get-Date: A positional parameter cannot be found that accepts argument '09:32'.
```

>PowerShell assumes that because we didn't specify `AM` or `PM`, we are using a 24 hour time format.

To specify the time to be `09:32 PM`, add the _PM_ inside the quotes.

```pwsh
Get-Date "07/04/1776 09:32 PM"
```

## Something Useful: Finding Completion Dates

Everything explained up to this point is interesting, but not useful. How can it be applied to a real,
everyday problem? A common task for project managers is creating project plans. Plans can range from
a fully detailed Gantt chart or a list of milestones and associated completion dates. During project
planning, for a particular task there is a start date and an estimated duration, usually measured in
weeks or days. The equation for finding the completion date is
`start date + estimated duration = completion date`. A project manager may find herself using this
equation repeatedly while planning a project. You can use PowerShell to find completion dates. If
the start date is July 4, 2023 and the estimated duration is eighty (80) days, the calculation in PowerShell
looks like:

```pwsh
(Get-Date 07/04/2023).addDays(80)
```

Results
```text
Friday, September 22, 2023 12:00:00 AM
```

The parentheses force the order of operations.
Inside the parentheses executes first, followed by the operation outside the parentheses.
The `.addDays()` part is called a *method*.
All dates created using `Get-Date` have this and many other methods _built-in_.

An abbreviated list of methods for dates:

+ AddDays
+ AddHours
+ AddMilliseconds
+ AddMinutes
+ AddMonths
+ AddSeconds
+ AddYears
+ Equals
+ GetDateTimeFormats
+ IsDaylightSavingTime

There are no _Subtract_ methods.
To subtract days, use a negative value in the `.AddDays()` method.
Subtracting days helps with finding the start date given a completion date and an estimated duration.
For example, you need a task to be completed by July 4th and it will take eighty days to complete.
When should you start the task?
Find the date that was eighty (80) days before July 4, 2023 like this:

```pwsh
(Get-Date "07/04/2023").AddDays(-80)
```

Result:
```text
Saturday, April 15, 2023 12:00:00 AM
```

Start the task on Tax Day in the US!

## What About Weeks?

So far, the examples add and subtract days, but what if you want to calculate using _weeks_?
There is no `.AddWeeks()` method.
However, you can take the number of weeks, multiply by seven (7), and use the `AddDays()` method to calculate in weeks.
Find the date 5 weeks in the future from 11/23/2023:

```pwsh
(Get-Date 11/23/2023).AddDays(5*7)
```

Result:
```text
Thursday, December 28, 2023 12:00:00 AM
```


## Find The Time Between Dates

In the last section, the _date math_ calculates a date in the past or future given a start date and an elapsed number of days (or months or seconds).
What if you have two dates and need to find the time _between_ those dates?
PowerShell can handle that problem.
Both dates must be created using the `Get-Date` technique [described before](#creating-a-specific-date).

If you want to know the amount of time between July 4, 2023 and October 31, 2023, type this:

```pwsh
(Get-Date "07/04/2023") - (Get-Date "10/31/2023")
```

Result:
```text
Days              : -119
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 0
Ticks             : -102816000000000
TotalDays         : -119
TotalHours        : -2856
TotalMinutes      : -171360
TotalSeconds      : -10281600
TotalMilliseconds : -10281600000
```

All the values are negative.
This means that the order of the dates matters.
Swap the dates to make the times positive.

```pwsh
(Get-Date "10/31/2023") - (Get-Date "07/04/2023")
```

Now the results are positive values:
```text
Days              : 119
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 0
Ticks             : 102816000000000
TotalDays         : 119
TotalHours        : 2856
TotalMinutes      : 171360
TotalSeconds      : 10281600
TotalMilliseconds : 10281600000
```

Notice the use of parentheses in the calculations.
The date must be "created" before the subtraction operation.

## Conclusion

The objective of this article was to introduce non-technical users to a single useful PowerShell feature.
You should now have the confidence to:

+ Open PowerShell
+ Create a Date with or without a time of day.
+ Add or Subtract Days, Hours, Months, etc. from the Date
+ Create two dates and find the time span between them.

## References

[^1]: [Microsoft PowerShell Overview](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.3)
[^2]: [Get-Date Help](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-date?view=powershell-7.3)
[^3]: [PowerShell About Case-Sensitivity](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_case-sensitivity?view=powershell-7.3)