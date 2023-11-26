#!/usr/bin/python3
"""..."""


def text_indentation(text):
    """"..."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ws = 0
    while ws < len(text) and text[ws] == ' ':
        ws += 1

    while ws < len(text):
        print(text[ws])
        if text[ws] == "\n" or text[ws] in ".?:":
            if text[ws] in ".?:":
                print("\n")
            ws += 1
            while ws < len(text) and text[ws] == ' ':
                ws += 1
            continue
        ws += 1
