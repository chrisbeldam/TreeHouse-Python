favourite_things = ["raindrops on roses", "whiskers on kittens", "bright copper kettles", "warm woolen mittens", "bright paper packages tied up with string",
"cream coloured ponies", "crisp apple studels"]

favourite_things[1:5] #  Returns 2, 3, 4, 5. Starts : Ends - Excludes item at the end

favourite_things[:2] # First two items
favourite_things[1:] # Up to the Ends
favourite_things[:] # Returns a copy of the list

string = "hello"
string[0:2] # Returns he

# Slices That Skip

numbers = list(range(20)) # 0 - 19
numbers[::2] # Even numbers whole lists
numbers[2::2] # Excludes 0
numbers[-2:] # Last two in the list
numbers[-2:-5:-1] # Goes back through the list by 1 from 18

# Deleting/Replacing Slices

rainbow =  ["red", "orange", "green", "yellow","blue", "black","white", "aqua", "purple", "pink"]
del rainbow[5:8] # Deletes 5,6,7
rainbow[2:4] = ["yellow", "green"] # Swaps them
