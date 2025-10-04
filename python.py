# basic
print("hello world!")

#Input 
name = Input("enter name :")
print("Hello",name )

# variables
x = 10 # int
y = 3.14 # float
name = "Fatima" # string
is_on = True # boolean

#Data structures
list1 = [1,2,3] # list
tuple1 = (1,2,3) # tuple
set1 = {1,2,3} # set
dict1 = {"a":1,"b":2} # dictionnary

#conditionals
if x>5:
    print("big")
elif x==5:
    print("equal")
else:
    print("small")


#Loops
for i in range(5):
    print(i)

while x>0:
    x -= 1


#imports
import math
print(math.sqrt(16)) # 4.0


#Methods
def greet(name):
    return "Hi" + name

greet_msg = greet("Fatima")
print(greet_msg)  #Hi Fatima


#Classes
class Dog:
    def __init__(self, name):
        self.name = name
    def bark():
        print("Woof Woof")

d= Dog("Max")
d.bark() #woof woof

