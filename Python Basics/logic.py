True + True # Equals 2

bool(True)
bool(False)

bool([]) # Anything empty is considered False
bool("Whoo") # Would be true

5 == 5 # True
1 == 7 # False
5 != 7 # True
5 < 7 # True

a = 5
b = 5

a == b # True

c = []
d = []

c == d # True

e == None # Both would be true
e is None


# If this Then That

a = 10
b = 4

if a > b:
    print("hello!")

age = 19 * 365

if age > 10000:
    print("Wow, over 10000 days old!")

else:
    print("You are not old enough")

age = 220000

if age> 20000:
    print("time to retire")

elif age > 10000:
    print("long time left")

else:
    print("Time to get started")

# Containment - In

"cheese" in "cheeseshop" # Returns true

cheeseshop = []
"cheese" in cheeseshop # Returns false

if "cheese" in cheeseshop:
    print("Woo we have some cheese")

else:
    print("we have run out of cheese")


# Loops

for name in ["Bob, Emily, Chris"]:
    print("Hello " + name)

x = 10

while x < 10:
    print(x)
    x+=1

# Inputs

input("What is your age?: ")
age = int(input("What is your age?: "))
age + 1

# Custom Functions

def hows_the_parrot():
    print("He's pining for the fjords!")

hows_the_parrot()

def lumberjack(name, prounoun):
        print("{} 's a lumberjack and {} ok").format(name, prounoun)
lumberjack("chris", "he's")
lumberjack("sam", "she's")

def average(num1, num2):
    return(num1+num2) /2

avg = average(10,10)
print(avg)


# Exceptions
try:
    count = int(input("Give me a number: "))

except ValueError:
    print("Thats not a number!!!")
else:
    print("Hi" * count)
