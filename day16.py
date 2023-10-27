#______Lists________

marks=[3,5,6, "Yo", True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3]) #negative indexing
print(marks[len(marks)-3])


if 6 in marks:
    print("yes")
else:
    print("no")  #check whether an item is present in the list.

if "Prashant" in marks:
    print("yes")
else:
    print("no")


'''
   * Lists are used to store multiple items in a single variable.

   *  Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are 
    Tuple, Set, and Dictionary, all with different qualities and usage.

   * Lists are created using square brackets[]:

'''