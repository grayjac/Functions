#!/usr/bin/env python3


# ME499-S20 Python Lab 1 Problem 2
# Programmer: Jacob Gray
# Last Edit: 4/6/2020


def letter_count(text, letter):
    """
    Returns the number of letter occurrences in the text, n. Detection is case sensitive.
    :param text: String of text.
    :param letter: String of one letter.
    :return: Number of letter occurrences in the text.
    """
    if not isinstance(text, str) or not isinstance(letter, str):
        raise TypeError  # Raises TypeError if text or letter isn't a string

    n = 0  # Setting number of letter occurrences in text to zero

    for cursor_letter in text:
        if cursor_letter.lower() == letter or cursor_letter.upper() == letter:
            n += 1

    return n
