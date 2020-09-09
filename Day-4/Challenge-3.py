shopping_list = []  # empty list created


def show_list():
    # prints out the list contents
    print("Here is your list")
    for index, item in enumerate(shopping_list, start=1):
        print(index, ":", item)


def show_help():
    print("Enter 'DONE' to stop adding")
    print("Enter 'SHOW' to see your list items")
    print("Enter 'REMOVE' to remove item from the list at a specific index")
    print("Enter 'HELP' to see this help")
    print("What should we pick at the store?")


def add_to_list(new_item):
    shopping_list.append(new_item)



print("Menu\n-------------------------------------------------------------------")
show_help()
print("What should we pick at the store?")

while (True):
    new_item = input("=> ")

    if not new_item:
        continue
    elif (new_item.upper() == 'DONE'):
        break
    elif (new_item.upper() == 'SHOW'):
        show_list()
        continue
    elif (new_item.upper() == 'HELP'):
        show_help()
        continue
    elif new_item.upper() == 'REMOVE':
        item_number = int(input("Which item to remove, number please: "))
        shopping_list.pop(item_number-1)
        continue
    else:
        if new_item not in shopping_list:
            add_to_list(new_item)

print("Here is your list of items:")

for index, item in enumerate(shopping_list, start=1):
    print(index, item)
