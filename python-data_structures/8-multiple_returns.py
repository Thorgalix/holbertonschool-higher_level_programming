#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    long = len(sentence)
    firstchar = sentence[0]
    return (long, firstchar)
