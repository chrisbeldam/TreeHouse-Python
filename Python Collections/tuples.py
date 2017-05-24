# my_tuple = (1,2,3)
# my_second_tuple = 1,2,3
# tuple = tuple([1,2,3])
#
# tuple_with_a_list = (1,"apple", [3,4,5])

#Packing Tuples

a = 5
b = 20

a,b = b,a # Swaps values

def add(*nums):
    total = 0
    for num in nums:
        total+=num
    return total

add(4,4)

#Multiple Return Values

def packer(**kwargs): # ** packs the variables which are parsed
    print(kwargs)



def unpacker(first_name = None, last_name = None):
    if first_name and last_name:
        print("hi {} {}".format(first_name, last_name))
    else:
        print("Hi no name")

packer(name="Kenneth", num=42, spanish_inquisition=None) #Prints it out as a dictionary
unpacker(**{"last_name": "Love", "first_name": "Kenneth"})

course_minutes =  {"Python Basics": 232, "Django Basics": 237, "Flash Basics": 189, "Java Basics:" 133,}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course, minutes))
