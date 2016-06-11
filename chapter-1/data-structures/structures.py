# So now we know how to store data into variables, now we are gonna
# store many variables into collections

# Lists: you can put whatever you want into lists by keeping all the data between
# [ ] and separated by commas, e.g:

my_list = [1, 'two', 3.2] # here we are creating a list what has one integer, one string and
# one float

# let's print that out
print "My First List:"
print my_list

# we can also store variables in lists

first_variable = 1
last_variable = 'test'

my_other_list = [1, 'test']

print "My list from variables"
print my_other_list


# Operations on lists
# lets create a new list

new_list = [1,3,4]
# We can access to the element on the given position of a list by doing
print "New list on the first position"
print new_list[0] # here we are accessing to the first position of the list
# remember that the first position is 0, not 1
# so 0 => 1, 1 => 3, 2 => 4

print "From position 1 to 3"
print new_list[1:3]  # pretty cool eh?

# We can also join two lists

first_list = [1,2]
second_list = ['three', 'four']

print "Joining Lists"
print first_list + second_list
