# Sample Input Validators #

This directory contains the input validator for the "Pirate Coin Hunt" problem.
We only ship a single validator, written in the checktestdata format (`validate.ctd`).
The validator enforces the exact contest constraints:

- First line: `N k` where `1 ≤ N ≤ 1 000 000` and `1 ≤ k ≤ 10^18`.
- Second line: exactly `N` integers `gᵢ` with `1 ≤ gᵢ ≤ 10^9`.
- No extra tokens or trailing input.

