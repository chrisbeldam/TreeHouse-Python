# Dictionaries

#Dicts are not sorted

course = {"title": "Python Collections"}
course["title"] # Returns python Collections

dict([["name":"Kenneth"]]) # Bad way to create dictionary

course = {"title": "Python Collectiosn", "teacher":"kenneth Love", "videos": 22}
course["videos"] # Returns 22

course = {"title": "Python Collectiosn", "teacher":["first_name" :"kenneth", "Last_name": "Love"], "videos": 22} # Dictionaries inside of dictionaries

kenneth = {"first_name":"Kenneth", "job":"teacher"}
kenneth["Last_name"] = "love" # Adds this key and value to dictionary

kenneth.update({"job": "python teacher", "editor":"vs"}) # Adds more than one key and value to the dictionary

#Packing and Unpacking Dictionaries

def packer(**kwargs): # ** packs the variables which are parsed
    print(kwargs)

packer(name="Kenneth", num=42, spanish_inquisition=None) #Prints it out as a dictionary

def unpacker(first_name = None, last_name = None):
    if first_name and last_name:
        print("hi {} {}".format(first_name, last_name))
    else:
        print("Hi no name")

#Dictionary Iteration

course_minutes =  {"Python Basics": 232, "Django Basics": 237, "Flash Basics": 189, "Java Basics:" 133}

for course in course_minutes:
    print(course_minutes[course]) # Prints just the course minutes

for key in course_minutes.keys():
    print(key) # Prints keys

for value in course_minutes.values():
    print(values) # Prints values

for items in course_minutes.items():
    print(item)
