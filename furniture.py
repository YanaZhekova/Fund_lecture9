import re

command = input()
furniture_list = list()
total_price = 0
while command != "Purchase":
    matches = re.finditer(r">>(?P<furniture>[A-Z]+[a-z]*)<<(?P<price>[0-9]+[.]?[0-9]*)!(?P<quantity>[0-9]*)", command)

    for match in matches:
        furniture = match.group("furniture")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))

        furniture_list.append(furniture)
        total_price += quantity * price

    command = input()
print("Bought furniture:")
for f in furniture_list:

    print(f)

print(f"Total money spend: {total_price:.2f}")