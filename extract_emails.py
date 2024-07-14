import re

text = input()

matches = re.finditer(r"[^-._\w+](?P<user>([a-zA-Z]+[0-9]*[-_.]*)\w+)@(?P<host>[a-zA-z]+[-.]?[a-zA-z]+[-.]*[a-zA-Z]*[.][a-zA-Z]*)[^-._,]", text)
for match in matches:
    print(match.group().strip())
