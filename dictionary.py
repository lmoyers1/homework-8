######################################################################################################
# File: dictionary.py
# Date: Feb 10, 2020
# Author: Monica Ihli monica@utk.ed
# Description: Demonstrates a variety of ways to create, use, and access dictionaries.
######################################################################################################




print('################## CREATING A DICTIONARY ##############')

# create a simple dictionary/home/monica/Dropbox/Python_Course/feb-10/dictionary.py
# /home/monica/Dropbox/Python_Course/feb-10/format.py
# /home/monica/Dropbox/Python_Course/feb-10/input.py
# /home/monica/Dropbox/Python_Course/feb-10/lists.py
# /home/monica/Dropbox/Python_Course/feb-10/sets.py
staff_dict = { 'id_code' : 'mktg1234', 'name' : 'Samantha', 'years': 3}
print(staff_dict) # print the whole dictionary

# other syntax for creating a dict & probably the LEAST typing:
staff_dict = dict(id_code='mktg1234', name='Samantha', years=3)

# and yet another way
staff_dict = dict([('id_code', 'mktg1234'),('name', 'Samantha'), ('years',3)])


print('################## ACCESSING DATA WITHIN A DICTIONARY ##############')

print(staff_dict['id_code']) # prints the value associated with the key that you just gave it
print(staff_dict['name'])
print(staff_dict['years'])

# This line would break if you uncommented it. You can't reference a key that doesn't exist:
# print(staff_dict['not_existing'])

# use dictionary values in expressions, the same as any other
if staff_dict['years'] < 2:
  print('Employee has been here less than 2 years')
elif staff_dict['years'] >= 3:
  print('Has been employed at least 3 years.')
else:
  pass  # pass means "do nothing" in a place where some response is required


print('################## UPDATING  ##############')

# update value based on key
staff_dict['name'] = 'Molly'
print(staff_dict['name'])

# easily add another dictionary element after the fact
staff_dict['vacation'] = '2 weeks'
print(staff_dict)

print('################## DELETING DATA ##############')

# delete dictionary elements
del staff_dict['id_code'] # remove entry
print(staff_dict)

staff_dict.clear()     # remove all entries in dict
print(staff_dict)

del staff_dict # delete the entire dictionary


meal_plan_dict = dict(Monday='meatloaf', Tuesday='enchiladas', Wednesday='pizza night', Thursday='roast beef',
                      Friday='lasagna')


print('################## ITERATING OVER ITEMS ##############')

# .items() returns a list of key-value pairs in the dict
print(meal_plan_dict.items())
for item in meal_plan_dict.items(): # these can be accessed individually
  print(item) # items look like ('key', 'value')


# accessing individual keys and values when iterating with .items()
for key, value in meal_plan_dict.items():
  print("On {} we will serve {}.".format(key,value))
# list of dictionaries


# get a sequence of just keys
dict_keys = meal_plan_dict.keys()
print(dict_keys)

# get a sequence of just values
dict_values = meal_plan_dict.values()
print(dict_values)


print('################## LIST OF DICTIONARIES ##############')


# notice how we are declaring a list, then each item in the list is a dict
my_cats = [
  dict(name='Salsa', age='7', color='black'),
  dict(name='Zippy', age='6', color='black'),
  dict(name='Velvet', age='7', color='gray')
]

print(my_cats)

# iterating over every dictionary in the list to access values
for cat in my_cats:
  print('I have a cat named {} who is {} years old.'.format(cat['name'], cat['age']))


# accessing dictionary values directly based on their positional index in the list:
print(my_cats[0]['name'])
print(my_cats[1]['name'])
print(my_cats[2]['name'])



