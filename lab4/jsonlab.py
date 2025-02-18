import json

with open("sample-data.json", "r", encoding="UTF-8") as json_file:
    data = json.load(json_file)

print('''Interface Status
=======================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------ ''')

for i in data["imdata"]:
    i = i["l1PhysIf"]["attributes"]
    print(i["dn"].ljust(51), end="")
    print(i["descr"].ljust(21), end="")
    print(i["speed"].ljust(10), end="")
    print(i["mtu"].ljust(8), end="")

    print()