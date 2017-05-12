favourite_number = 14

del favourite_number # This would delete the variable

# Numbers

5 + 5
10 - 2
11 * 2
10 / 5

5 + (5 * 2) # Specifies order we want

# Age Calculation

years = 19
days = years * 365
weeks = days / 7

# Lists

list = [1,2,3,4,5]
list = list + [6,7] # Add to the list
list * 2 # Repeats the list twice

list.append(8) # Adds the number 8 to the end of the list
list.extend([9,10]) # Will add multiples numbers into the list and will only be a single list
list.remove(6) # Removes this number from the list

#Splits

list("hello")
"hello".split() # Splits white space
"hello there students".split() # Splits into three words
"red:blue:green".split(":") # Splits on :

#Joins - Only works on string items

flavours = ["Chocolate", "mint", "strawberry"]
", ".join(flavours) # Adds a space after comma
"my favourite flavours are: " + ", ".join(flavours)

# Index

alpha = "abcde"
alpha.index("a") # Returns index of the first instance of "a"
alpha_list = list(alpha)
alpha_list.index("b") # returns 1
alpha.index("cd") # returns 2 as it starts at position 2
alpha[0] # returns A

# Index - Deletion
trash = 99
del trash # deletes variable

alpha_list = list("abcde")
del alpha_list[2] # deletes c
