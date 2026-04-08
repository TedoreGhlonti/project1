import sys

reverse_words = []

words = sys.argv[1:]

for w in words:
    word = w[::-1]

    reverse_words.append(word)

print(reverse_words)