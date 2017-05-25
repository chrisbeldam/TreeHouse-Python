import pdb

# logging.warning("The french have the grail")
# logging.info("info")

#Python Debugger


my_list = [5,2,1,True,"abcdefg",3,False,4]

pdb.set_trace() # Debugger - Need to remove when done

del my_list[3] # Deletes True
del my_list[3] # Deletes String
del my_list[4] # Deletes False
print(my_list)
