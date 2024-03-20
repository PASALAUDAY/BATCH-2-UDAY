# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# s1 = "Hello how are you"
# s2 = "Hello how is"

#s1 = "Hello how are you"
#s2 = "Hello how is "

#s1 = s1.split(" ")
#s2 = s2.split(" ")

#for val in s1:
#    if val not in s2:
#        print(val)
#for val in s2:
#    if val not in s1:
#
#print(val)

# 3.)Wrire a code print the 8th fibanochi number
# 0,1,1,2,3,5,8

# ! Find the 8th fibanochi number
# num = 8
# n1 = 0
# n2 = 1

# for val in range(num):
 #   ans = n1+n2
 #   n1 = n2
 #  n2 = ans
 #   print(ans)

# ! Constructors
# ? Eg:2
# * unparametarised constructor
#class profile:
 #   def _init_(self):
#        print("hello world")
#obj = profile()
#obj._init_()
 
#? Eg: 3
# * Parametarised constructor
#class profile:
#    def __init__(self,id,name,age):
#       print(id,name,age)

#obj = profile(1,"uday",30)        

# ? Eg:4
#class c1:
#    email = "uday@gmail.com"
   
#    def m1(self):
#         name = "uday"
#         place = "kadapa"
#         print(name,place)
#         print(self.email)
        
        
#object = c1()    
#object.m1()

# ? Eg:5
#class c1:
#    email = "uday@gmail.com"
    
#    def m1(self):
 #       name = "udy"
  #      age = 28
   # def display(self):
        # ! print(name,age)
        # ! print(self.name,self.age)
    #    print(self.m1())
        
#object = c1()
#object.display()

# ? Eg:6
# ? To use the variable inside the constructor in another methods
#class class1:
   # email = "udy@gmail.com"   #static variable
#def _init_(self):
#  self.name = "udy"
#  self.email = "udy@gmail.com"
  # return name, email # error --> cannot use return with construct

#def display(self):
#    print(self.name,self.email)

#c1 = class1()
#c1.display()

# ! ----> Inheritance
# The process of utilising the methods and attributes of parent class
# throught the object of child class it is called as inheritance

# ? 5 types of Inheritance
# Single Inheritance
# Multilevel Inheritance
# Multiple Inheritance
# Hybrid Inheritance
# Heirarichal inheritance

# * single Inheritance
# ? It has only one parent class and only one child class
# ! Eg:1
#class parent:
#    def m1(self):
#        print("Iam parent class")


#class child(parent):
#    def m2(self):
#        print("Iam child class")
#obj = child()
#obj.m1()

# Hybrid Inheritance
# The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
class c2:
    def m2(self):
        print("class2")
class c3:
    def m3(self):
        print("Class 3")
class c4:
    def m4(self):
        print("Class 4")
class c5:
    def m5(self):
        print("Class 5")
class c6:
    def m6(self):
        print("Class 6")




















