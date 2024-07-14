import re

text = input()
while text != "":
    matches = re.finditer(r"(?P<sub_domain>w{3})[.]{1}(?P<domain>[a-zA-Z]+[0-9]*([-]?)[a-zA-Z]*[0-9]*\3?[a-zA-Z]+[0-9]*)[.]{1}(?P<domain_extension>[.]*[a-zA-Z]+)+",text)
    for match in matches:
        print(match.group())
    text = input()


