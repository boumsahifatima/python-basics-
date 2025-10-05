# output
print("hello world!")

#Input 
name = input("enter name :")
print("Hello",name )

# variables
x = 10 # int
y = 3.14 # float
name = "Fatima" # string
is_on = True # boolean

#Data structures

# list

list1 = [1,2,3] 
list1.index(1) # 0
list1.append(4) # 1 2 3 4
list1.extend([4,5]) # 1 2 3 4 5
list1.insert(1,0) # 1 0 2 3
list1.remove(1) # 2 3 
list1.pop(1) # 1 3
list1.count(3) # 1
list1.reverse() # 3 2 1

# tuple

tuple1 = (1,2,3) 
tuple1.count(3) # 1
tuple1.index(1)  # 0


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

