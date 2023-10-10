#_______________String_Methods____________

a="prashant!!!!"

print(len (a))

print(a.upper()) # used to convert text to uppercase.
print(a.lower()) # used to convert text to lowercase.

print(a.rstrip("!")) # used to remove particular characters.
print(a.replace("prashant","Bohra")) # used to replace characters.

print(a.split(" ")) # used to split string in list
print(a.capitalize()) # used to capitalize first letter of string in a paragraph.


print(a.count("prashant")) # used for counting a particular character/word in a paragraph.

str1="My name is Prashant Bohra."

print(str1.find("is")) # this method searches for the first occurrence of the given value and return the index where it is present.


'''  ___________MORE METHODS IN PYTHON__________

   isalnum() =true only if the string contains A-Z, a-z, 0-9. No special characters
   isalpha() =true only if the string contains A-Z, a-z. No special characters and numbers.
   islower() =true only if the string contains lowercase characters.
   isupper() =true only if the string contains uppercase characters.
   isspace() =true only if the string contains whitespaces else false.
   swapcase() = uppercase of the string converts to lowercase and lowercase into upper.
   title() =  capitalize each first letter in a word in a string.

'''