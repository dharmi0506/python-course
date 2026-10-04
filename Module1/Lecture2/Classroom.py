#introduction line
# print("Hello Dharmi from Sandeep")

# #1-------->How to print Multiple Values together<----------------------

# # " " represents text or String

# print(2 + 3) #5


# print("How old is Dharmi?") 

# print("Dharmi's Age : ",11)

# print("my grade: ",6 ,", my tag: ",61)
#  #my grade : 6 , my tag: 61
# # to write multiple values in one print statement we can separate values using comma(,)

#2------------>\n(new line character)<------------------

# print("Dhami Patel") #Dharmi Patel

# print("Dharmi\nPatel") #Dharmi
#Patel

#3------------->Default end = \n of print statement<----------


# print("Dharmi")
# print("Patel")
#Output for top 2 lines : #Dharmi
#Patel


# print("Dhami",end=" ") 
# print("Patel",end = "\n")
#Output for above 2 lines : Dharmi,end=

#4--------->Identifiers<-------------
#Definition : 
#Naming Rules : Letters(A-Z) and (a-z) and numbers(any number) are allowed and _(underscore is allowed).

#tell if these are valid names:
# a  --- allowed
# abc --- allowed
# a10 --- allowed
# a_10 --- allowed
# a-11  --- not allowed because of -
# a$11  --- not allowed because of $ sign
# a@11 --- not allowed because of @ sign       

# 123a -----> It can't start with a number

# a b ----------> NO space allowed

#5---------->Variable<----------

#A labelled space that can hold value and change.

# x = 10
# y = 20
# print(x + y) #30

# x = 15
# print(x + y) #35

#6----------->KeyWords<------------------

# Keywords : Reserved words used in any programming language

import keyword
print(keyword.kwlist)