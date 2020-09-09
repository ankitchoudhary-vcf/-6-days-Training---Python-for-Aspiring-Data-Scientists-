shopping_list = []  # empty list created

print("What should we pick at the store?")
print("Enter 'DONE' to stop adding")

while (True):
    new_item = input("=> ")

    if not new_item:
        continue
    if (new_item.upper() == 'DONE'):
        break
    if new_item not in shopping_list:
        shopping_list.append(new_item)

print("Here is your list of items:")

for index, item in enumerate(shopping_list, start=1):
    print(index, item)
