
import json
from datetime import datetime

with open("operations.json","rt") as file:
    content = file.read()

# print(content)
    # for el in file:
    #     print(el)
    #     print()

content = json.loads(content)
# print(content[1])
# print()
# print(content[1]['operationAmount']['currency'])

executed_operations_list = []

for i in content:
    item = i.get('state', 'no info')
    # print(item)
    # print()
    if item =='EXECUTED':
        executed_operations_list.append(i)


#print(executed_operations_list)

thedate = datetime.fromisoformat(content[1]['date'])
thedate2 = datetime.fromisoformat(content[2]['date'])

# print(thedate<thedate2)
# print(thedate)

dlin = len(executed_operations_list)

for i in range(dlin - 1):
    for j in range(dlin - i - 1):
        if datetime.fromisoformat(executed_operations_list[j]['date']) > datetime.fromisoformat(executed_operations_list[j + 1]['date']):
            executed_operations_list[j], executed_operations_list[j + 1] = executed_operations_list[j + 1], executed_operations_list[j]

# print(executed_operations_list[:-6:-1])
# print()
for i in executed_operations_list[:-6:-1]:
    print(f"{i['date']} {i['description']}")
    print(f"{i.get('from', 'no info')} - {i['to']}")
    print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
    print()


























