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
    print("no")

if "Prashant" in marks:
    print("yes")
else:
    print("no")