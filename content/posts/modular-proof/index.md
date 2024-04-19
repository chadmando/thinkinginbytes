+++
categories = [ "technology" ]
title = "Proving Congruence For Fun"
description = "Proof of a congruence theorem in modular arithmetic."
slug = "proving-congruence-for-fun"
date = "2024-04-19T02:38:46.343Z"
lastmod = "2024-04-19T02:38:50.905Z"
tags = [ "mathematics", "LaTeX" ]
draft = false
+++

## Background

I want to understand the math behind asymmetric cryptography.[^1]
This field relies heavily on Modular Arithmetic.[^2]
I bought an undergraduate math textbook for self-study.
This article is a record of a proof exercise in the book.
It is also a good exercise in writing math equations using LaTeX.
> NOTE: I asked ChatGPT to confirm the proof.
> No grades are being assigned here, the point is to learn.

## Problem

Let \\(m\geq1\\) be an integer.

(a) If \\(a_1\equiv a_2 \pmod{m}\\) and  \\(b_1\equiv b_2 \pmod{m}\\), then

\\(a_1\cdot b_1\equiv a_2\cdot b_2 \pmod{m}\\)

## Proof

The definition of congruence:
m divides \\(a_1-a_2\\)
In an equation this can be written as:
$$a_1=a_2+k\cdot m$$
and
$$b_1=b_2+j\cdot m$$

If we multiply the right and left sides of these equations:
$$a_1\times b_1=(a_2+km)\times(b_2+jm)$$

Use the FOIL method for multiplying binomials.

$$a_1\times b_1=a_2\times b_2+a_2\times jm+b_2\times km+km\times jm$$

We now consider each term in this equation \\(\pmod{m}\\)
All of the terms with that are multiples of m will drop out of the equation since for any integer x: \\(x\times m \pmod{m}\\) is zero.
This leaves the final equation as:
$$a_1\times b_1=a_2\times b_2 \pmod{m}$$

## References

[^1]: Wikipedia [article](https://en.wikipedia.org/wiki/Public-key_cryptography) references Public-Key Cryptography which is directly linked from asymmetric cryptography.
[^2]: Wikipedia information on [Modular Arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic)
