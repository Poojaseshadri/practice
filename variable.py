"""valid variable name"""
myVariable = "pooja"
my_variable = "pooja"
_my_variable = "pooja"
myvariable = "pooja"
MYVARIABLE = "pooja"
myvariable2 = "pooja"
print(myVariable)
print(my_variable)
print(_my_variable)
print(myvariable)
print(MYVARIABLE)
print(myvariable2)

"""invaid variable name"""
"""1myvariable = "pooja"
my-variable = "pooja"
my variable = "pooja"

print(1myvariable)
print(my-variable)
print(my variable)"""  """SyntaxError: invalid syntax"""

x="this"
y="is"
z="pooja"
print(x,y,z)
print(x+y+z)

x = 5
y = "Pooja"
#print(x + y)
print(x,y)

#global variable
x = "day"
def myfunc():
  x = "pooja"
  print("This is " + x)
myfunc()
print("Have a good " + x)