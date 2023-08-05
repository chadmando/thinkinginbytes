+++
categories = [ "technology" ]
title = "Asking AI About Password Length - Part 3"
description = "A conversation with Google's Bard about password length limits"
slug = "asking-ai-about-password-length-part-3"
date = "2023-08-05T13:15:20.859Z"
tags = [ "AI", "password", "LLM", "Bard" ]
draft = false
+++

In Part 3, I ask Google's [Bard](https://bard.google.com) why _it_ would limit password length to 15 characters in a web application.
See [Part 1](https://thinkinginbytes.com/posts/asking-ai-about-password-length-part-1/) for the response from Anthropic's Claude and [Part 2](https://thinkinginbytes.com/posts/asking-ai-about-password-length-part-2/) for ChatGPT's _thoughts_ on the subject.
I start with the same question.

## Starting Prompt
Me:

_You are a web application developer. I am an information security professional reviewing your work. Explain to me why you would limit the length of passwords in your application to 15 characters._


Bard:
>Hi information security professional,
>
>Thank you for reviewing my work. I understand that you are concerned about the password length limit of 15 characters. I would like to explain why I have chosen this limit.
>
>A longer password is not always more secure. While it is true that a longer password provides more entropy, which makes it more difficult to guess, it also makes it more difficult for users to remember. This can lead to users choosing weaker passwords that they can easily remember, such as their pet's name or their birthday.
>A 15-character password is still secure enough. A 15-character password that is made up of a variety of characters (uppercase and lowercase letters, numbers, and symbols) is still very difficult to guess, even with a brute-force attack. In fact, a study by Google found that a 12-character password would take an average computer over 10 years to crack.
>There are other security measures in place. In addition to the password length limit, my application also has other security measures in place, such as two-factor authentication and password expiration. These measures help to further protect user accounts, even if a password is compromised.
>I understand that you may still have concerns about the password length limit. However, I believe that the security benefits of a 15-character password outweigh the risks. I am always open to feedback, so please let me know if you have any other suggestions.
>
>Thank you for your time.
>
>Sincerely,
>
>Web Application Developer

## Bard's Initial Theories
The response was more formal.
I do love Bard's argument that, "A longer password is not always more secure."
Bard's initial reasons for limiting password length are:

1. User Experience (Easier to Remember)
1. 15 Characters Is _Secure Enough_
1. Defense In Depth (Two-Factor Authentication and Password Expiry)

Me:

_There is no two-factor authentication or password expiry included in your application. Are there any technical reasons for the password character limit?_

Bard:
>Yes, there are some technical reasons why I might limit the password length in my application even if there is no two-factor authentication or password expiration.
>
>Legacy systems. If my application interacts with legacy systems that do not support long passwords, I may need to limit the password length to ensure compatibility.
>Performance. Hashing and storing long passwords can take more time and resources, which could impact the performance of my application.
>Usability. Long passwords can be more difficult for users to remember and type, which could lead to users choosing weaker passwords or forgetting their passwords altogether.
>In general, I would recommend setting a password length of at least 12 characters, even if there are no other security measures in place. However, there may be some cases where a shorter password length is necessary for technical reasons.
>
>If you are concerned about the security of your application, I would recommend implementing two-factor authentication and password expiration, even if you are limiting the password length. These measures can help to further protect user accounts, even if a password is compromised.

Compatibility with legacy systems compatibility is a common reason between Bard and ChatGPT.
Bard insists that people can't remember long passwords, so there is no reason to offer longer password length.
Bard didn't try to convince me that SHA was an acceptable password hashing algorithm.

## Bard's Theories

The final list from Bard looks like this:

1. 15 Characters Is _Secure Enough_
1. Defense In Depth (Two-Factor Authentication and Password Expiry)
1. Compatibility With Legacy Systems

Bard also mentioned twice that humans can't remember long passwords and this should be considered in the design of the application.

## Bard's Non-Reasons

There were two reasons that longer passwords aren't needed in an application.

1. Defense In Depth (Two-Factor Authentication and Password Expiry)
1. Humans Can't Remember Long Passwords