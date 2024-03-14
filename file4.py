#  -----> while loop
#  -----> break using while loop

# eg:1
# 1.) Iterate from 20to 30 and break the loop in 27

#i =20
#while i<31:
 #   if i ==27:
 #break
 #   print(i)
 #   i+=1

# 2.)
# =20
#while i<31:
#    print(i)
#    i+=1
#     if i ==27:
 #       break


# 3.)
#i=20
#while i<31:
 #   print(i)
 #   if i==27:
 #       break
 #   i+=1

# 4.)
#i=20
#while i<31:
 #   if i==27:
 #      print(i)
#       break
 #   i+=1


# ! ------> continue
# ----> Eg:1
#i =20
#while i<31:
#    if i==27:
#        continue
#    print(i)
#    i=i+1

# ! ----> continue
# -----> Eg:1
#i =20 
#while i<31:
#    i=i+1
 #   if i==27:
 #       continue
 #   print(i)
# ! Eg:
# while to iterate from 12 to 22
# find the sum of all numbers

#i=12
#sum=0
#while i<=22:
#    sum=sum+i
#    i=i+1
#print(sum)

# ! Eg:6
# find the average of value from 20 to 25

#i=20
#sum=0
#count = 0
#while i<=25:
#    sum=sum+i
#    count+=1
#    i+=1
#print(sum/count)

# ! -------> Nested for loop
# Eg:1

#for row in range(1,3+1):
  #  for col in range(1,4+1):
 #       print(row,col)

# Eg:2
# * * * *
# * * * *
# * * * *
# * * * *


#for row in range(4):
 #   for col in range(4):
 #       print("* * * * *", end=" ")

#sum =0
#for row in range(5):
 #   for col in range(5):
#        sum= sum+1
#       print(sum, end=" ")
        
 #   print()


# !to print stars in right angled triangle

#for row in range(0,6):
#    for col in range(0, row):
 #       print("*", end=" ")
  #  print()    
   

#* * * * * *
#* * * * *
#* * * *
#* * *
#* *
#*
 
#for row in range(0,6):
 #   for col in range(row,6):
 #       print("*", end=" ")
 #   print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *       


#for row in range(5):
 #   for col in range(5):
#        if col==0 or col==5-1 or row ==0 or row ==5-1:
#            print("*", end=" ")
#        else:
 #           print(" ", end=" ")
 #   print()


#         *
#       * * *
#      * * * *
#     * * * * *


#for row in range(0,5):
#    for col in range(0,6):
 #       if ((row==0 and col==3) or (row==1 and(col>2 and col<=4)) or (row==2 and (col>=1 and col<=5))):
#           print("*", end=" ")
 #       else:
#           print(" ", end=" ")
#    print()


# *
# * *
# *   *
# *     *
# *       *
# * * * * * *     


#for row in range(0,6):
#    for col in range(0,5):
 #       if ((row==1 and col==0) or (row==1 and (col>=2 and col<=4)) or (row==2 and (col>=3 and col<=6))):
 #           print("*",end=" ")
#        else:
 #           print(" ",end=" ")
#print()


#Number --> int, float complex
# String
# Boolean
# None
# Collection
# List
# tuple
# set
# dictionary

# ? --> List

# 1.) if the collection of elements are sorrounded by square brackets, it is considered
# to be list
# ! eg:
    # 11 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]

# characteristics of list
# 1.) list have to be sorrounded by []
# 2.) it is mutable (the elements in the list are changable)
# 3.) Every element inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

# To access the elements in list
#11= [1, 4, 1, 7,89.7, 715, "p", "i"]
 # print(11)

# ---> Indexin
#In the collection datatypes like list, tuple, string, the elements will be allowed
# with predefines unique value called index value

# we have 2 types of indexing
# positive indexing ---> starts with 0 from left hand side
# Negative indexing ---> starts with -1 from right hand side

# ?--> Positive indexing
# print(1st1[0])
# print(1st1[4])
# print(1st1[20]) --> error

# ?---> Negative indexing
lst1= [1, 4, 1, 7,89.7, 7.5, "p", "1"]
# print(1st1[-1]) I
# print(1st1[-5])

# ? ---> slicing
# lst1= [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# 1st1[start_index:end_index: step]

# print(lst1[0:4])
# print(lst1[6:8])
# print(lst1[3:6])
# print(lst1[:5])
# print(lst1[3:])
# print(lst1[:1])

#print(lst1[0:7:1]) # lst1[0:7] ---> both are same
#print(lst1[0:7:2])

# trail int(input())


lst1= [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# print(lst1[-4:-1])
# print(1st1[-1:-4]) --> []
# print(1st1[-7:-1])
print(lst1[-7-1:2])











