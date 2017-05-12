# favourite_things = ["raindrops on roses", "whiskers on kittens", "bright copper kettles"]
# favourite_things += ["warm woolen mittens"] # Permanently adds it to the list
# favourite_things.append(["bright paper packages tied up with string"])
#
# del favourite_things[-1] # Deletes the last item in the list
#
# favourite_things.append("bright papaer packages tied up with string") # Also works
#
# favourite_things.extend(["Cream coloured ponies", "crisp apple strudles"]) # Extends our existing list
#
# favourite_things.insert(1, "whiskers on kittens") # Adds the string in at position 1(2)

#Shopping List 3

#make a list to hold onto our items

shopping_list = []


def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")


def add_to_list(item):
    shopping_list.append(new_item)
    print("Added! List has {} items.".format(len(shopping_list)))


def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)


show_help()

while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)

show_list()

# Remove from the list

# alpha_list ["a","z","b","c","d"]
# del aplha_list[2]
#
# my_list = [1,2,3,1]
# my_list.remove(1) # only removes first value
# my_list.remove(1)
