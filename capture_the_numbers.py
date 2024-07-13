import re

text = input()
output = list()
while text != "":
    matches = re.findall(r"\d+", text)
    for match in matches:
        output.append(match)
    text = input()

print(" ".join(output))