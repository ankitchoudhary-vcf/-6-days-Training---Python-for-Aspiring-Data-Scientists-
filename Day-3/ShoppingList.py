"""
Challenge 1
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.

Hint 1
#pseudocode 
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""
shopping_list = [] #empty list created

print(
  """
  What should we pick at the store? 
  Enter 'DONE' to stop adding

  """
)

while (True):
  new_item = input("Next item: ")

  if not new_item:
    continue
  if (new_item.upper() == 'DONE'):
    break
  if new_item not in shopping_list:
    shopping_list.append(new_item)

print ("Here is your list of items:")

for index, item in enumerate(shopping_list, start = 1):
  print (index, item)