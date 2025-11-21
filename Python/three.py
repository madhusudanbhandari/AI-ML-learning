#while loop
# count=1
# while count<=5:
#     print('hello')
#     count+=1
# print(count)

# i=0
# while(i<=10):
#     print(i)
#     i+=1

# i=10
# while i>=1:
#    print(i)
#    i-=1

# i=1
# while(i<=10):
#     print(i*5)
#     i+=1

# i=1
# list=[]
# while(i<=10):
#     list.append(i**2)
#     i+=1
# print(list)

# list=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i=0
# while i<len(list):
#     print(list[i])
#     i+=1


# list=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i=0
# x=36
# while i<len(list):
#     if(list[i]==x):
#      print('found at index',i)
#     else:
#        print('finding')
#     i+=1


#BREAK AND CONTINUE 
#break is the keyword that is used to terminate the loop when encountered

# i=0
# while i<=10:
#     print(i)
#     if (i==3):
#         break
#     i+=1
# print("end of loop")

#continue: igonres the execution of the current iteration and starts executing from the next iteration

# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1

# i=0
# while(i<=10):
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1





####FOR LOOOP
# list=[1,4,67,78,34]
# for el in list:
#     print(el)

# list=[1,2,3,4,5,6,7,8,9,10]
# for el in list:
#     if(el%2==0):
#         print(el)

# tup=(1,2,3,5)
# for el in tup:
#     print(el)

# list=[1,2,3,4,5]
# for el in list:
#     if(el%2==0):
#      print(el)
     # else:
#     print('end')



# list=[1,4,9,16,25,36,49,64,81,100]
# for wl in list:
#     print(wl)

# list=[1,4,9,16,25,36,49,64,81,100]
# x=36
# indx=0
# for el in list:
#     if(el==x):
#         print(el ,'found at', indx)
#     indx+=1


##Range: range is the function that by default starts with 1 and increments by 1 untill the second last number in the specified range


# for i in range(5):
#     print(i)

# seq=range(3,8,2)
# for i in seq:
#     print(i) 

# for i in range(11):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# for i in range(11):
#     print(i*5)

#pass statement : passs is a null statement that does nothin.it is used as a placeholder for a future code
# for el in range(10):
#   pass

#

#wap to find sum of first n numbers(using while)
# i=0
# a=0
# while i<=10:
#     a=a+i
#     i+=1
# print(a)

#factorial of first n numbers
# fact=1
# for i in range(5,0,-1):
#     fact=fact*i
#     print(i)
# print(fact)







#function is a block of statement that performs a set  of specific task
# def sum(a, b):
#     s=a+b
#     return s
# print(sum(2,3))

# def dif(a,b):
#     return a-b
# print(dif(5,1))
 
# def hel():
#     print('hello')
# hel()

# def avg(a,b,c):
#     return (a+b+c)/3
# print('average of three numbers is',int(avg(5,6,4)))


#functions are of two types
#1. Built in functions
#2.user defined functions
 

#default parameter:paarameters that are used when there are  no values passed as an argument

# def sum(a=4,v=2):
#     return a+v
# print(sum(2))

#wap to print the length of the list as a parameter

# def leng(list):
#     return len(list)
# print(leng([3,4,5,67,8,2]))

#waf to print the elements of a list in a single line
# num=[3,56,7,24,89]
# def count(list):
#     for i in list:
#         print(i,end=" ")
# count(num)

#waf to find the factorial of n


# def factorial(n):
#     fact=1
#     for i in  range(1,n+1):
#         fact=fact*i
#     print(fact)
# factorial(5)


#conv usd to npr
# def conv(usd):
#     npr=usd*140
#     return npr
# print(conv(4))

# def sep(n):
#     if(n%2==0):
#         print('even')
#     else:
#         print('odd')
# num=int(input('enter a number'))
# sep(num)


###REcursion:recursion is the function which calls itself repeatedly
# def recur(n):  #function
#     if(n==10):
#         return 
#     print(n)
#     recur(n+1)  #recursive
# print(recur(5))

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
 
# print(fact(5))

#factorial
# def fact(n):
#     if (n==0 or n==1):
#         return n
#     else:
#         return n*fact(n-1)
# print(fact(5))



#sum of first n nu,bers

# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)
# print(sum(5))


#write a recursive function to print the all elements in list
# def print_list(list,indx):
#     if indx==len(list):
#         return 0
#     print(list[indx])
#     print_list(list,indx+1)

# print_list([1,3,4,4,6,7],0)





###File input output:python can be used to perform operations on the file
 ##we have to open a file before reading and writing

# f=open('file.txt','r')
# print(f.read())
# #print(type(data))
# f.close()

# f=open('file.txt','r')
# print(f.read(5))
# f.close()

# f=open('file.txt','r')
# print(f.readline())
# f.close()


# f=open('file.txt','w')
# f.write('hiiii')

# f=open('file.txt','a')
# f.write('hello')



# f=open('file.txt','r+')
# f.write('madhu')
# print(f.read())
# f.close()

# f=open('file.txt','w+')
# #print(f.read())
# f.write('hello')
# print(f.read())


#with function
# with open('file.txt','r') as f:
#     data=f.read()
#     print(data)


##deleting a file using os module
#module is basically like a core library that is written by another programmer which we can use'
# import os
# os.remove('file.txt')
#here os is a module

# fi=open('file.txt','w')
# fi.write('hello')


# f=open('practice.txt','w+')
# f.write('hi everyone \n we are learning file i/o \nusing java \ni like prog in java \n' )


# with open('practice.txt','r') as f:
#     val=f.read()

# new_val=val.replace('python','java')
# print(new_val)
# with open('practice.txt','w') as f:
#  f.write(new_val)

    
# with open('practice.txt','r') as f:
#     val=f.read()
#     print(val)
# if(val.find('learning')!=-1):
#     print('found')
# else:
#     print('not found')


# def check_for_line():
#     word='python'
#     data=True
#     line_no=1
#     with open('practice.txt','r') as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1

#     return -1

# print(check_for_line())
               

#wap to count even numbers fromm the file
# count=0
# with open('file.txt','r') as f:
#     data=f.read()

# val=data.split(',')
# for nums in val:
#  if(int(nums)%2==0):
#     count+=1
# print(count)
