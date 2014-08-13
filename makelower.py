import sys

with open('dictionary.txt', 'r') as f:
    with open('dict.txt', 'w') as output:
        for string in f:
            output.write(string.lower())
