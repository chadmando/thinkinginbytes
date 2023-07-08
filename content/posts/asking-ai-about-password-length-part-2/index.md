+++
categories = ['technology']
title = "Asking AI About Password Length - Part 2"
description = "A conversation with ChatGPT about password length limits"
slug = "asking-ai-about-password-length-part-2"
date = 2023-07-07
tags = ['AI','password','LLM','ChatGPT']
draft = false
+++

In [Part 1](https://thinkinginbytes.com/posts/asking-ai-about-password-length-part-1/), I asked Anthropic's Claude AI Assistant to play _Web Application Developer_ and explain why it would choose to limit its application's password length to no more than 15 characters.

In this post, I used the same starting prompt and asked ChatGPT.

## Starting Prompt 
Me:

_You are a web application developer. I am an information security professional reviewing your work. Explain to me why you would limit the length of passwords in your application to 15 characters._

ChatGPT:
>As an information security professional, I understand the importance of strong and secure passwords to protect user accounts from unauthorized access. However, limiting the length of passwords to 15 characters in a web application may seem counterintuitive or raise concerns. Let me explain the reasons why a password length limit of 15 characters may be implemented:
>
>Compatibility with Legacy Systems: In some cases, web applications may be integrated with legacy systems or databases that have predefined limitations on password length. These limitations could be technical constraints or requirements set by the system's architecture. As a result, the web application would need to enforce the same password length limit to ensure compatibility and seamless operation with these existing systems.
>
>Hashing Algorithm Limitations: Many web applications use hashing algorithms to store user passwords securely. These algorithms generate fixed-length hash values regardless of the password length. If the hashing algorithm used has a fixed output length, such as 128 or 256 bits, enforcing a password length limit can prevent potential issues that may arise from longer passwords. Longer passwords would be truncated or require additional processing, which can introduce complexity and potentially weaken the security of the hashing mechanism.
>
>User Experience Considerations: While longer passwords generally provide increased security, they can also be more difficult for users to remember and type accurately. By imposing a reasonable length limit, such as 15 characters, web applications aim to strike a balance between security and usability. This ensures that users can create passwords that are strong enough to resist common attacks while still being manageable for them.
>
>Avoiding Denial of Service (DoS) Attacks: By setting a maximum password length, a web application can prevent potential denial of service attacks that malicious actors might attempt by submitting excessively long passwords. Limiting the length ensures that server resources are not unnecessarily consumed or overwhelmed during the authentication process.
>
>While a password length limit of 15 characters may appear restrictive compared to more common recommendations for longer passwords, it is important to note that other security measures should be implemented to compensate for this limitation. These measures may include enforcing complexity requirements (e.g., a mix of uppercase and lowercase letters, numbers, and special characters) and facilitating two-factor authentication to enhance the overall security of user accounts.

## ChatGPT's Theories

Unlike Claude, ChatGPT jumps right into the reasons for password length limits.

1. Compatibility With Legacy Systems
1. Hashing Algorithm Limitations
1. User Experience (Easier To Remember)
1. Denial of Service Protection

## Store Hashes, Not Passwords

Me:

_I don't understand the reasoning in your item 2.  If, as you said, the hashing algorithm generates a fixed-length value regardless of the password length, then why would the length of the password need to be limited?_

ChatGPT:
>Apologies for any confusion caused. You are correct that hashing algorithms generate fixed-length hash values regardless of the input password length. In that context, the length of the password itself does not directly affect the length of the hash output. However, there can still be indirect implications related to the password length limit. Let me clarify the reasoning behind item 2:
>
>Storage Space: While the hash output is of fixed length, the storage space allocated to store the hashed password can be a consideration. If a web application has a predetermined storage size for the hashed password field, exceeding this size due to excessively long passwords could cause storage or database-related issues. Therefore, imposing a password length limit ensures that the storage space requirements for hashed passwords remain consistent.
>
>Performance and Processing: While the length of the password doesn't impact the length of the hash output, longer passwords can require more computational resources and time to process during the hashing operation. If passwords beyond a certain length are permitted without limitation, it may open up the potential for resource-intensive attacks, such as using extremely long passwords to deliberately exhaust server processing capabilities. By setting a reasonable length limit, web applications can mitigate these performance-related risks and maintain efficient processing of passwords.
>
>It's important to note that the specific reasoning behind implementing a password length limit of 15 characters may vary depending on the context of the application, its architecture, and the underlying systems it interacts with. The examples provided are meant to illustrate some general considerations that might lead to such a decision.

## Storage Space Makes No Sense
Me:

_Regarding item 1 in your last response, explain how long passwords would make the hash value larger and violate the established store space._

ChatGPT:
>I apologize for the confusion caused in my previous response. I misspoke regarding the impact of password length on hash value size and storage space. Please disregard that statement.
>
>In reality, the length of the password does not directly affect the size of the hash value or violate the established storage space. Hash functions, regardless of the input length, produce a fixed-length output. So, the size of the hash value remains constant, regardless of the password length.
>
>I apologize for the incorrect information provided earlier. The primary reason for limiting the length of passwords in a web application is usually related to compatibility with legacy systems or to strike a balance between security and usability, as mentioned earlier. It is not directly related to the storage space or hash value size.
>
>Thank you for pointing out the error, and I apologize for any confusion caused.

## Password Hashing Is Slow, On Purpose

Me:

_You mentioned Performance and Processing as having an indirect effect on computational resources.  Isn't it true that the hashing algorithms that are suitable for passwords are intentionally slow to prevent brute force attacks?  Most of these algorithms re-hash the hash value so after the initial hashing operations, all processing time becomes the same for any password length._

ChatGPT:
>You are correct, and I apologize for any confusion caused by my previous response. The performance and processing considerations I mentioned do not directly relate to the length of the password, but rather to the computational resources required for hashing operations.
>
>Hashing algorithms suitable for password storage are indeed intentionally designed to be slow and computationally intensive to mitigate brute force attacks. These algorithms typically involve multiple iterations and utilize techniques like key stretching and salting to increase the time required to calculate the hash value.
>
>Once the initial hashing parameters, such as the algorithm, iterations, and salt, are established, the processing time for subsequent hashing operations remains relatively consistent regardless of the password length. The length of the password itself does not significantly impact the processing time beyond the initial hashing.
>
>Therefore, I apologize for any confusion caused by my previous response, and I appreciate your clarification. The primary reasons for limiting password length in a web application typically revolve around compatibility, user experience, and avoiding potential denial of service attacks, rather than the direct impact on computational resources or hash processing time.

## Combined List Of Reasons

Merging answers from [Claude](https://thinkinginbytes.com/posts/asking-ai-about-password-length-part-1/#claudes-theories) and [ChatGPT](#chatgpts-theories) and eliminating wrong suggestions gives this list:

1. Client-side input field limitations
1. Buffer Overflow protection
1. Denial of Service (DoS) protection
1. Coding Convenience (Developer's Choice)
1. Compatibility With Legacy Systems
1. Hashing Algorithm Limitations
1. User Experience (Easier To Remember)

## Apology Count

ChatGPT apologized six times for causing confusion or providing incorrect information.
