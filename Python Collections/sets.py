
{1,3,5} # Is a set
{} # Dictionary not a set

low_primes = {1,3,5,7,11,13}
low_primes.add(17) # Adds to the set
low_primes.update({19,23},{2,29})
low_primes.discard(100) # Removes

#Maths

set1 = set(range(10))
set2 = {1,2,3,5,7,11,13,17,19,23}
set.union(set2) # Combines

set1|set2 # Same as above

set.difference(set2)
set2.difference(set1)

set1 - set2 # difference

set1 ^ set2 # unique
