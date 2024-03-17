+++
categories = [ "technology" ]
title = "A Piecewise Hashing Example"
description = "A simple example of piecewise hashing by block size using python"
slug = "piecewise-hashing"
date = "2024-03-17T15:40:04.479Z"
lastmod = "2024-03-17T15:40:16.318Z"
tags = [ "hashing", "malware", "python" ]
draft = false
preview = "/content/posts/piecewise-hashing/thinkinginbytes_github_template.png"
+++
<!-- TOC -->

- [The Problem](#the-problem)
- [Cryptographic Hashing](#cryptographic-hashing)
- [What Is Piecewise Hashing](#what-is-piecewise-hashing)
- [The Obvious Weakness](#the-obvious-weakness)
- [Final Thoughts](#final-thoughts)
- [References](#references)

<!-- /TOC -->

>NOTE:
>ChatGPT was used to create some portions of the code in this article.  The words are mine.

## The Problem

When cybersecurity analysts find malicious files, they share their finding with the greater security community.
They run the file through a cryptographic hashing function and share the results of this function, called a _hash_.
The hash is a kind of _fingerprint_ that identifies the file based on the information contained in the file.
Others can look through their environments, hash their files, and compare the results to hunt for the malicious file.


To make life difficult for defenders, the bad guys change a small part of their malware.
It doesn't take much.
Adding whitespace or a comment alters the file, which changes the hash.
Even though the malware functions the same, the signature used to detect it changes.

## Cryptographic Hashing

A full explanation of cryptographic hashing is outside the scope of this post. Wikipedia has an article that describes the properties of a cryptographic hash function.[^1]

## What Is Piecewise Hashing

Piecewise hashing is hashing different _pieces_ of the file.
By comparing the hashes from chunks of the file, we can identify identical sections.
To create a simple example, a string is used in place of a file.
The process of piecewise hashing is the same whether it is a string of bytes or a binary file.

Take the following byte strings in python:

```python
first_file = b"The rain in Spain falls mainly on the plain."
second_file = b"The rain in Spain falls mostly on the plain."
```

This string `first_file` is 44 bytes long.
The string `second_file` is 44 bytes long.
Hashing the strings shows their different fingerprints.

```python
import hashlib

first_hash = hashlib.md5(first_file).hexdigest()
second_hash = hashlib.md5(second_file).hexdigest()
```

Printing both hashes shows the difference between them.

```text
>>> first_hash
'3948716d567532d9aee33c7d2f34b970'
>>> second_hash
'33af9610767a566786f205bc2798d0c9'
```

Piecewise hashing can help us determine if any parts of `first_file` and `second_file` are the same.
First, we need a function to take a string and hash every 8 bytes.

```python
import hashlib
from collections import OrderedDict

def hash_byte_sections(byte_data, BLOCK_SIZE=8):
    """
    Takes a byte string or bytearray, hashes every BLOCK_SIZE bytes using the SHA1 algorithm,
    and stores the hashes in an ordered dictionary.
    
    Parameters:
    - byte_data: The byte string or bytearray to be processed.
    - BLOCK_SIZE: The size of the blocks to hash, default is 8 bytes.
    
    Returns:
    - An OrderedDict where each key is a tuple indicating the byte section (start, end)
      and each value is the corresponding SHA1 hash of that section.
    """
    
    if isinstance(byte_data, bytearray):
        byte_data = bytes(byte_data)
    
    hash_dict = OrderedDict()
    
    for i in range(0, len(byte_data), BLOCK_SIZE):
        section = byte_data[i:i+BLOCK_SIZE]
        hash_value = hashlib.md5(section).hexdigest()
        hash_dict[(i, i+BLOCK_SIZE)] = hash_value
    
    return hash_dict
```

Before the hashing begins, we should understand what will be hashed.
By printing the blocks for both byte strings, it is easy to see which blocks should have the same hash.

```bash
>>> for i in range(0, len(first_file), 8):
...     section = first_file[i:i+8]
...     print(f'BlockID:{i} {section}')
...
BlockID:0 b'The rain'
BlockID:8 b' in Spai'
BlockID:16 b'n falls '
BlockID:24 b'mainly o'
BlockID:32 b'n the pl'
BlockID:40 b'ain.'
>>>
>>>
>>> for i in range(0, len(second_file), 8):
...     section = second_file[i:i+8]
...     print(f'BlockID:{i} {section}')
...
BlockID:0 b'The rain'
BlockID:8 b' in Spai'
BlockID:16 b'n falls '
BlockID:24 b'mostly o'
BlockID:32 b'n the pl'
BlockID:40 b'ain.'
>>>
```

Based on the _pieces_ of each string, `BlockID:24` should yield different hashes.

Here is a comparison of the hashes:

```text
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Section  ┃ Hash 1                                   ┃ Hash 2                                   ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ (0, 8)   │ 282ecfc53331f9f3ca62d8fcce43f5aab2e3fc97 │ 282ecfc53331f9f3ca62d8fcce43f5aab2e3fc97 │
│ (8, 16)  │ 114692ba9e0ead94834be6e9fd72392712362261 │ 114692ba9e0ead94834be6e9fd72392712362261 │
│ (16, 24) │ 34e9ff1e4013fcc34f53db23cc3f73983416503d │ 34e9ff1e4013fcc34f53db23cc3f73983416503d │
│ (24, 32) │ d3f243aad4a102497838ed4192fe5a1b281c110e │ 934957ccae2e3daccdce860342d9c230d1eb9fa5 │
│ (32, 40) │ dc445c795e8059532276b06d48889202066f62fc │ dc445c795e8059532276b06d48889202066f62fc │
│ (40, 48) │ 940998818acf17d7bdf93273d29f2004dbaefa37 │ 940998818acf17d7bdf93273d29f2004dbaefa37 │
└──────────┴──────────────────────────────────────────┴──────────────────────────────────────────┘
```

## The Obvious Weakness

There is an obvious weakness with piecewise hashing based on a block size.
Any new data added skews the sections and no hashes will match.

In our example, if `second_file` was changed to:

```python
second_file = b"Yo! The rain in Spain falls mostly on the plain."
```

Every block is different from `first_file`.

```bash
>>> for i in range(0, len(second_file), 8):
...     section = second_file[i:i+8]
...     print(f'BlockID:{i} {section}')
...
BlockID:0 b'Yo! The '
BlockID:8 b'rain in '
BlockID:16 b'Spain fa'
BlockID:24 b'lls most'
BlockID:32 b'ly on th'
BlockID:40 b'e plain.'
```

And if none of the blocks contains identical data, no hashes will match.

```text
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Section  ┃ Hash 1                                   ┃ Hash 2                                   ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ (0, 8)   │ 282ecfc53331f9f3ca62d8fcce43f5aab2e3fc97 │ bdebd188ba898ee015353929760915df70ba2680 │
│ (8, 16)  │ 114692ba9e0ead94834be6e9fd72392712362261 │ bcf704412b3b2a54aabeec0808f7121095591462 │
│ (16, 24) │ 34e9ff1e4013fcc34f53db23cc3f73983416503d │ 5acf81033c8b4aa7b0b8c7faca26ce82715e5239 │
│ (24, 32) │ d3f243aad4a102497838ed4192fe5a1b281c110e │ 7191da4765df51a1fd5eada0d5ac3a5c0c4eb491 │
│ (32, 40) │ dc445c795e8059532276b06d48889202066f62fc │ 54bfba16f6e9ee060e0ad6f1f9453f5afd0b197c │
│ (40, 48) │ 940998818acf17d7bdf93273d29f2004dbaefa37 │ 4271afeb901e39256c30d5419ad07e4726451698 │
└──────────┴──────────────────────────────────────────┴──────────────────────────────────────────┘
```

This makes piecewise hashing ineffective at determining if any part of the two files (strings in the example) are similar.
Even if we compared _any_ `first_file` hash to _any_ `second_file` hash, there are no matches.

## Final Thoughts

This article was more about satisfying my curiosity with creating a simple piecewise hashing script in python.
Software exist that perform fuzzy matching of files[^2] like the example presented here.
The ssdeep project uses a different method of piecewise hashing called Context Triggered Piecewise Hashing (CTPH).[^3]
A simple example of CTPH using python is a topic for another article.

## References

[^1]: Wikipedia article on [cryptographic hash functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function).
[^2]: The package [ssdeep](https://ssdeep-project.github.io/ssdeep/index.html) can perform fuzzy matching.
[^3]: [Digital Investigations Journal article](https://www.sciencedirect.com/science/article/pii/S1742287606000764?via%3Dihub) by Jesse Kornblum; September 2006