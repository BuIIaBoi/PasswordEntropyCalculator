# Password Entropy Calculator

A command-line tool that estimates a password's strength using Shannon entropy, based on character-set size (uppercase, lowercase, digits, symbols) and length.

## How to Run

1. Make sure Python is installed.
2. Open a terminal in this folder.
3. Run: `python Project_v3.py`
4. Enter a password when prompted (input is hidden as you type, like a login prompt).

## What to Expect

1. The program calculates the password's entropy in bits.
2. If entropy is below 35 bits, it explains which changes (length, character variety) would strengthen it.
3. Otherwise, it reports the password strength as OK.

## Known Limitations

- This measures theoretical entropy assuming the character set used is random — it doesn't check the password against known breached-password lists or common dictionary words, both of which matter more in practice than raw entropy.
