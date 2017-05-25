import datetime

# print(datetime.datetime.now())
#
# treehouse_start = datetime.datetime.now()
#
# treehouse_start = treehouse_start.replace(hour =9, minute=0, second=0, microsecond=0) # Replaces attributes of the datatime object
#
# datetime.datetime.now() - treehouse_start # Returns a timedelta (days, seconds, microseconds)
#
# time_worked = datetime.datetime.now() - treehouse_start
# time_worked.convert.day() # Returns days
# time_worked.seconds() # Returns seconds
# hours_worked = round(time_worked.seconds/3600) # Returns the hours

#Time Deltas

# now = datetime.datime.now()
#
# datetime.timedelta(days=3)
#
# now + datetime.timedelta(days=3) # Adds 3 days
#
# now + datetime.timedelta(days=-5) # Removes 5 days
#
# now - datetime.timedelta(days=5) #- 5 Days
#
# now.date() # Returns time
# now.time() #Returns time
#
# hour = datetime.timedelta(hours=1)
#
# workday = hour * 9
#
# tomorrow=datetime.datime.now().replace(hour=9, minute=0) + datetime.timedelta(days=1) # Tomorrow

#Today & tomorrow

# now = datetime.datetime.now()
# today = datetime.datetime.today() #Only difference is the seconds

# today = datetime.datetime.combine(datetime.date.today(), datetime.time()) # Returns a midnight version of today
#
# today.weekday() # Returns 2 - Wednesday
#
# now.timestamp() # Returns a float

#Dating Methods


# now = datetime.datetime.now()
# now.strftime('%B %d') # Month, Day
# now.strftime('%m/%d/%y') # Month, Day, Year
#
# birthday = datetime.datetime.strptime('2015-04-21', '%Y-%m-%d')

#Wikipedia

answer_format = "%m/%d"
link_format = "%b_%d"

link = "https://en.wikiedpia.org/wiki/{}"

while True:
    answer = input("What date would you like?")
    if answer.upper() == "QUIT":
        break

    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print("That is not a valid date")
