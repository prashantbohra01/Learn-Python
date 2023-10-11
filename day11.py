#____________Match_Case____________________

# Example 1
x=int(input("Enter value for match_case: "))

match x:
      case 0:
            print("X is zero")
      case 1:
            print("X is one")
      case _:
            print(x)

'''we have to first pass a parameter then try to check with which case the parameter
   is getting satisfied. If we find a match we will do something and 
   if there is no match at all we will do something else.
'''

# We can use if else also in match case.