+++
categories = [ "technology" ]
title = "Manually Enroll Windows Device Into Autopilot"
description = ""
slug = ""
date = "2025-08-16T04:24:13.408Z"
lastmod = "2025-03-09T14:33:16.816Z"
tags = [ ]
draft = true
preview = "@static/img/thinkinginbytes_feature_image.png"
+++


## Assumptions

1. You have a new, Windows 11, PC at the Out-Of-Box-Experience (OOBE)
1. Your organization has an Intune subscription
1. You have EntraID permissions to add a device to AutoPilot (e.g. Intune Administrator)
1. You have an USB storage device to save the Diagnostic logs

## Steps

1. Boot new PC to the OOBE
1. Enter Diagnostics mode `Ctrl` + `Alt` + `D`
1. Export Logs to USB Storage
1. Identify the device hash `csv` file in the exported logs
1. Login to Intune
1. Navigate to Devices->Windows->Enrollment->AutoPilot Enrollment
1. 



## References

[^1]: Microsoft documentation [page](https://learn.microsoft.com/en-us/autopilot/add-devices)