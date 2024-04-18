+++
categories = [ ]
title = "Proving Congruence For Fun"
description = "Proof of a congruence theorem in modular arithmetic."
slug = "proving-congruence-fun"
date = "2024-04-18T02:57:32.764Z"
lastmod = "2024-01-01"
tags = [ "mathematics" ]
draft = true
+++

## Background

I want to understand the math behind asymetric cryptography.
This field relies heavily on Modular Arithmetic.
I bought an undergraduate math textbook for self-study.
This article is a record of a proof exercise in the book.
> NOTE: I asked ChatGPT to confirm the proof.
> No grades are being assigned here, the point is to learn.

## Problem

Let \\(m\geq1\\) be an integer.

(a) If \\(a_1\equiv a_2 \pmod{m}\\) and  \\(b_1\equiv b_2 \pmod{m}\\), then

\\(a_1\cdot b_1\equiv a_2\cdot b_2 \pmod{m}\\)

The definition of congruence:
m divides \\(a_1-a_2\\)
In an equation this can be written as:
$$a_1=a_2+k\cdot m$$

