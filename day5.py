#Type Casting or Type Conversion

a="5"
b="4"

print(a+b)

# if we add two strings values it will concatenate them together not add them
# so to avoid this type of problems we use TypeCasting or TypeConversion.

print(int(a) + int(b)) # This will give the correct result.

print("------------------------------------------------------------------------------")

# There are two types of TypeCasting and TypeConversion
# 1. Explicit TypeCasting
# 2. Implicit TypeCasting

# ----------------------------------------------------------------#

# Explicit TypeCasting
""" The conversion of one datatype into another by programmer intentionally as per the requirements
    is known as Explicit TypeCasting.
    It can be achieved by using builtin typecasting functions such as: int(), float(), hex(), str() etc.
    -----Example is shown above-----
"""

# Implicit TypeCasting
"""  When the data type conversion takes place during compilation or during the runtime, it's called an
     implicit data type conversion. 
     Python handles the implicit data type conversion, so we don't have to explicitly convert the data 
     type into another data type.
"""
# Example of Implicit DataType Conversion

c=3.2
d=4

print(" c is", c, type(c), "\n", "d is", d, type(d))

# Now both the Data types are different but Python will convert them automatically.

print( c+d, type(c+d))

