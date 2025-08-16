+++
categories = [ "technology" ]
title = "Specify Hugo Version In Netlify"
description = "Instructions on how to force Netlify to use a specific version of Hugo"
slug = "hugo-version-netlify"
date = "2024-10-16T03:17:01.193Z"
lastmod = "2024-10-16T03:17:03.917Z"
tags = [ "hugo", "netlify" ]
draft = false
preview = "@static/img/thinkinginbytes_feature_image.png"
+++


Thinkinginbytes.com is generated using [Hugo](https://gohugo.io) and hosted by [Netlify](https://www.netlify.com).
Netlify watches the [site's repo](https://github.com/chadmando/thinkinginbytes) on Github and commits trigger a site build process.
I'll post more details about hosting a Hugo site with Netlify later.
Site development is local.
To view the site on a local machine, Hugo must be installed.
It is likely that your local version of Hugo is versions ahead of the default Netlify Hugo version.
This version mismatch may cause Netlify builds to fail.
You may need to specify which version of Hugo you want Netlify to use.

## Netlify Site Configuration

First, login to Netlify and select your site.
Next, select `Site configuration`, then click Environment Variables.

{{< centeredimage src="netlify_siteconfig_env_variable.png" alt="Netlify Site Configuration" caption="Netlify Site Configuration" >}}

## Add Environment Variable

From Environment Variable, click on `Add a variable`, then `Add a single variable`.

{{< centeredimage src="netlify_envvar_addvar.png" alt="Netlify Environment Variable Add Variable" caption="Netlify Add Variable" >}}

## Create Variable

In the `Key` field enter "HUGO_VERSION".
The `Values` field should be the version of Hugo you want Netlify to build with.
Click `Create variable`.
Adding this Environment Variable will force the build process in Netlify to use the Hugo version you specified.

{{< centeredimage src="netlify_envvar_createvar.png" alt="Netlify Environment Variable Create Variable" caption="Netlify Create Variable" >}}

> NOTE: The version number should match the Hugo release information.

{{< centeredimage src="hugo_version_number.png" alt="Hugo Release Version Number" caption="Hugo Release Version Number Reference" >}}
