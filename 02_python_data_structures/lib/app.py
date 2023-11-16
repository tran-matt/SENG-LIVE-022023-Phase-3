# Sequence Types
#Note: use print() to execute the examples. Comment out examples after they've been demoed.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name 


#3. ✅ Return all pet names beginning from the 3rd index


#4. ✅ Return all pet names before the 3rd index
# print(pet_namems[:3])

#5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
#print(pet_names[3:7])

#6. ✅ Find the index of a given element
#print(pet_names.index('Luke'))

#7. ✅ Reverse the original list
#pet_names.reverse()
#print(pet_names)

#8. ✅ Return the frequency of a given element 


# Updating Lists
#9. ✅ Change the first element to all uppercase 


#10. ✅ Append a new name to the list
#pet_names.inserts(5,'Sally')
#pring(pet_names)

#11. ✅ Add a new name at a specific index


#12. ✅ Add two lists together 
#list_a = ["a","b", "c","d"]
#list_b = ["x","y","z","A"]

#list_c = list_a + list_b
#print(list_c)

#13. ✅ Remove the final element from the list
#pet_names.pop()
#print(pet_names)

#14. ✅ Remove element by specific index
#pet_names.pop(0)
#print(pet_names)

#15. ✅ Remove a specific element 
#pet_names.remove("Lea")
#print(pet_names)

#16. ✅ Remove all pet names from the list
#pet_names.clear()
#print(pet_names)

#Tuple 
# 📚 Review With Students:
    # Mutable, Immutable, Changeable, Unchangeable
pet_ages = (3,4,5,6,7,8,9)
#print(pet_ages)

#here we're making a constat version of a list

#17. ✅ Create a Tuple of pet 10 ages 
#print(pet_ages)

#18. ✅ Print the first pet age
#print(pet_ages[0])

# Testing Changeability 
#19. ✅ Attempt to remove an element with ".pop" (should error)
# pet_ages.pop()
#print(pet_ages)

#20. ✅ Attempt to change the first element (should error)
# pet_ages[0] = pet_ages[2]


# Tuple Methods
#21. ✅ Return the frequency of a given element
#print(pet_ages.count(4))

#22. ✅ Return the index of a given element 
#print(pet_ages.index(9))


#23. ✅ Create a Range 
#Note:  Ranges are primarily used in loops
#range_1 = range(10)
#print(range_1)

#when we say range of 10 it takes us back a range of what we're going to fit between

# Demo Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
my_set = {'a', 'b', 'c'}
print(my_set)


#arrays are always ordered but sets are not
#in sets numbers keep their places

#set is similar to an array with elements. a common example is when you try to have a list or array when elements are unique, they won't allow for duplicates to exist. A solution when there are duplicates is to take that array and make it a set and then convert it back to an array. It makes sure everything in there is unique.
# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'rose','age':11,'breed':'domestic long '}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_spot = dict(name='Spot', age=25, breed='boxer')


# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
#print(pet_info_rose['name'])

# when name is spelled wrong this means there are letter application break or we have to suppress the error types from occuring
# suppressing an error can create a domino effect of errors

#28. ✅ Print the pet attribute of "age" using ".get"
#Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error
#print(pet_info_rose.get('age'))

# if spelled wrong we'll get a "none" error

# this method is nice because it's a bit more descriptive

# Updating 
#29. ✅ Update the pets age to 12
#pet_info_rose["age"]=12
#print(pet_info)

#can't use .get and must use bracket notation

#30. ✅ Update the other pets age to 26
#pet_info_spot.update({'age':26})
#print(pet_info_spot)

# Deleting
#30. ✅ Delete a pets age using the "del" keyword 

#del pet_info_spot['ag']
#print(pet_info_spot)

#31. ✅ Delete the other pets age using ".pop"
#pet_info_rose.pop('ag')
#print(pet_info_rose)

#32. ✅ Delete the last item in the pet dictionary using "popitem()"


# Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
    ]

#33. ✅ Loop through a range of 10 and print every number within the range
#for num in range(10):
#    print(num)

#34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
for num in range(50,60, 2):
    print(num)

#35. ✅ Loop through the "pet_info" list and print every dictionary 
for pet in pet_info:
    print(pet)


#36. ✅ Create a function that takes a list as an argument 
    # The function should use a "for" loop to loop through the list and print every item 
    # Invoke the function and pass it "pet_names" as an argument

#def print_items(list):
 #   for item in list:
 #       print(item)

 #       print_items(pet_info)

#37. ✅ Create a function that takes a list as an argument. (simple example) 
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 

#def while_counter(pet_info):
#    count = 0 
#    while(count < len(pet_info) -1):
#       count += 1
#        print(count)

#while_counter(pet_info)
    

#38. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dict"s, "name" and "age" as parameters 
        # Create am index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'pet not found'

#def update_age(list, name, age):
#   index = 0
#    while index < len(list) - 1 and list[index].get('name') != name:
#        index += 1

#    if index < len(list):
#        list[index]['age'] = age
#        return list[index]
#    else:
#        return 'pet not found'


#print(update_age(pet_info, 'spot',26))

# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
# WHAT I WANT IN LIST - FOR ELE VAR NAME IN LIST VAR NAME]

#map = [pet.get('name').upper() for pet in pet_info]
#print(map)

# find like
#40. ✅ Use list comprehension to find a pet named spot
found = [pet for pet in pet_info if pet.get('name') == 'spot']
print(found)

# filter like
#41. ✅ Use list comprehension to find all of the pets under 3 years old
filter = [pet for pet in pet_info if pet.get('age') < 3]
print(filter)

#43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
pet_generator = (pet for pet in pet_info if pet.get('age') <3)
print(pet_generator)

#generator allows us to suspend list comprehension into a variable we can use later