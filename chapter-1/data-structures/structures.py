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


# We can also replace values on a given list

print "List without changes"
print first_list
first_list[0] = 10 # here we change the value on the first position with 10
print "List after the change"
print first_list


# Tuples

# A tuple is basically the same thing as a list, it keeps many values separated by commas
# but using ( ) instead of [ ], also we can't change the values or the size of the tuple

my_tuple = ( 'abc', 1, 1.2 )  # our first tuple

print "Printing tuple"
print my_tuple

print "Printing tuple at position"
print my_tuple[2] # we print our tuple at the position 2, that is 1.2

print "Print tuple from position 1 to 2"
print my_tuple[1:3]

# Dicts
# Dicts are dictionaries, this are different from lists b/c they have 2 values on each position
# a key and a value itself

harry = { 'name': 'harry', 'last_name': 'potter', 'wizard' : 'yes' }

# on each position we have two values, the ones before the : are called keys
# ( name, last_name, wizard ) and the ones after the colon are the values
# we can use the key to access the value of the dic

print "Print value of the dict under the name key"
print harry['name']
print "Same for last name"
print harry['last_name']
print "Is harry a wizard?"
print harry['wizard']

# We can also add keys to the dict by doing

harry['best_friend'] = 'Ron'

print "Who is Harrys best friend?"
print harry['best_friend']

# we have some operations over dics to access all the keys and all the values:

print "Dict keys"
print harry.keys()
print "Dict values"
print harry.values()
