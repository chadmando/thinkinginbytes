+++
categories = [ "technology" ]
title = "Manually Enroll Windows Device Into Autopilot"
description = "Learn how to manually enroll your Windows device into Autopilot using the hardware hash with this step-by-step guide."
slug = "manually-enroll-windows-device-autopilot"
date = "2025-11-09T20:50:48.865Z"
lastmod = "2025-11-09T20:50:54.695Z"
tags = [ "microsoft", "intune", "autopilot", "endpoint", "windows" ]
draft = false
preview = "@static/img/thinkinginbytes_feature_image.png"
+++


## Assumptions

1. You have a Windows 11 PC at the Out-Of-Box-Experience (OOBE)
1. Your organization has an Intune subscription
1. You have Entra ID permissions to add a device to Windows Autopilot (e.g. Intune Administrator)
1. You have an USB storage device to save the Diagnostic logs

> This is a restatement of the process outlined by Microsoft[^1].
> Those instructions lack a clear visual for navigating Intune.
>
> Microsoft recommends that this method only be used for testing or other limited scenarios.

## Steps

1. Boot new PC to the OOBE
1. Enter Diagnostics mode `Ctrl` + `Alt` + `D`
1. Export Logs to USB Storage
1. Identify the device hash `csv` file in the exported logs
1. Login to Intune
1. Navigate to Devices->Windows->Enrollment->Autopilot Enrollment
1. Import the csv file from the Diagnostics logs with the hardware hash.

{{< centeredimage src="intune_devices_enrollment_windows_autopilot.png" alt="Intune Windows Device Enrollment Flow" caption="Navigation to Intune Device Enrollment - Windows Autopilot" >}}

{{< centeredimage src="intune_devices_enrollment_windows_autopilot_import.png" alt="Windows Autopilot Device Enrollment Import" caption="Import .CSV With Hardware Hash" >}}

## References

[^1]: Microsoft documentation [page](https://learn.microsoft.com/autopilot/add-devices)
