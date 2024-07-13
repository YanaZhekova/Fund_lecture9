import re

text = input()

matches = re.finditer(r"\b(?P<user>[a-zA-z]*[0-9]*[-_.]?([a-zA-Z]*[0-9]*)?)@(?P<host>[a-zA-z]*-?.[a-zA-z]*(.[a-zA-Z]+)?)\b", text)
for match in matches:
    print(match.group())
