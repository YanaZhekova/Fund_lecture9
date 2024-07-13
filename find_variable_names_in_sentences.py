import re

text = input()

matches = re.finditer(r"\b_{1}(?P<name>[a-zA-Z]*|[0-9]+)\b", text)
output = list()
for match in matches:
    name = match.group("name")
    output.append(name)

print(",".join(output))
