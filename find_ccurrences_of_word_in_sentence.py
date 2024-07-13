import re

text = input()
find_word = input()

matches = re.findall(rf"\b{find_word}\b", text.lower())

print(len(matches))
