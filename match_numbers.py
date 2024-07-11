import re

text = input()

matches = re.finditer(r"(^|(?<=\s))(?P<numbers>-?([0-9]|[1-9][0-9]*)(.\d+)?)($|(?=\s))", text)
output = list()
for match in matches:
    output.append(match.group("numbers"))

print(" ".join(output))