# Brute-Force Time Estimator

## Overview
A Python-based cybersecurity script that utilizes combinatorics to evaluate password strength. By analyzing the character pool size and the length of the string, it calculates the total permutations (with repetition) and estimates the time required for a brute-force attack.

## The Math (Combinatorics)
The tool calculates the total sample space using the permutation formula for repeated elements: `Total Combinations = Pool_Size ^ Length`. 
For example, an 8-character password using only lowercase letters has $26^8$ (approx. 208 billion) combinations.

## Features
* Dynamically calculates character pool size based on user parameters (lowercase, uppercase, numbers, symbols).
* Simulates brute-force cracking speeds against modern GPU hash rates (10 Billion guesses per second).
* Converts raw computational seconds into human-readable timeframes (minutes, days, years).

## Proof of Work
Developed to demonstrate the practical application of probability, combinatorics, and large-scale sample spaces in software security and algorithm design.
