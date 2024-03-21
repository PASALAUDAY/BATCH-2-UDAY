# ! ------> Tasks
# Write the code for the bel tasks using function
# 1.) d1 {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
# a.) Find the min ans max priced product
# b.) Find the product starts with 's' and 'S'

# 2.) Find then 67, is strong number or not


# 3.) 11 [1,2,3,4,5,6]
# n=2--> [5, 6, 1,2,3,4]
# n=3--> [4,5,6, 1,2,3]

# ! Method riding
# * Ploymorphism in classes  using Inheritance
# Eg:1

#class bank:
#    def ratio(self):
#        print("All banks has repo rate")

#class SBI(bank):        
 #  def ratio(self):
 #      print("SBI rate is 9%")
             
#class IOB(bank):
#    def ratio(self):
 #       print("IOB rate is 7.5%")

#i = IOB()
#i.ratio()

#s = SBI()
#s.ratio()

# ? Eg:2
#class USA:
 #   def language(self):
 #       print("English")

  #  def capital(self):
  #      print("Washington DC")

   # class India(USA):
    #    def langauge(self):
     #       print("None")
            
      #  def capital(self):
       #     print("New delhi")

#I = India()
#I.langauge()
#I.capital()
       
# Eg:3
# Polymorphism using objects

#c1,c2 ---> c1 = print(c1),print(c2)
#f1,f2

# * Eg:4
#class c1:
#   def f1(self):
#        print("class 1")

#class c2(c1):
#    def f1(self):
#        super().f1()
#        print("class 2")


#obj1 = c2()
#obj1.f1()

#def display(a):
#      a.f1()
#display(obj1)
#display(obj2)

# * changing the functionality of builtin functions

#class shooping:
# class shooping:
#    def_ _init__(self, 11):
#      self.items = 11
#def _len_(self):
#length = len(self.items)
#return length
#s shooping ([1,2,3,4, 5])
#print(len(s))    

# ! ---> Method over loading
# ! Eg:1
#class suming:
 #   def add(self,a,b):
 #       print(a+b)

 #   def add(self,a,b,c):
  #      print(a+b+c)

#s = suming()
#s.add(4,3) # ! -----> error
#s.add(4,5,1)

# Eg:2
class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
           print(a+b+c)
        elif a!= None and b!=None:
             print(a+b)
        else:
            print(a)
            
obj= summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)





#a = 9
#b = 6
#print(a+b) 
#print(a.__add__(b)) # ? dunder method or mafic method

# int()
# print(a.__sub__(b))












