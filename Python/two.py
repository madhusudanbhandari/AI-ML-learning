#list=a built in datatype that stored the set of values separated by comma usually
#can store the elements of different datatypes
#mutable

# marks=[23,46.23,33,67,89,'ram','shyam']
# print(marks)
# print(type(marks))
# print(marks[2])
# print(marks[6])
# print(len(marks))
# marks[5]='sita'
# print(marks)
# print(marks[:4])
# print("my name is:",marks[5])


#list methods
# list1=[2,8,5]
# list1.append(6)
# print(list1)
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)
# list1.reverse()
# print(list1)
# list1.insert(3,'ram')
# print(list1)

# list=[2,1,3,1,5]
# list.remove(1)
# print(list)
# list.pop(2)
# print(list) 


#TUPLES; built in datatype That lets us create immutable sequennces of values
# tup=(1,2,3,8,4,5,2,2)
# print(tup)
# print(type(tup))
# print(tup[2])
# print(tup[1:3])

# print(tup.index(8))
# print(tup.count(2))


#wap to ask user to enter 3 movie names and store them in a list
# movie1=input("enter the first movie name:")
# movie2=input("enter the second movie name:")
# movie3=input("enter the third movie name:")
# movies=[movie1,movie2,movie3]
# print("the movies you entered are:",movies)
# print(type(movies))

#wap to check if a list contains a plaindrome of elements 
# list=['apple','ball','cat','cow','apple']
# list1=list.copy()
# list1.reverse()
# print(list)
# print(list1)
# if(list==list1):
#     print("the list is a plaindrome")
# else:
#     print("the list is not a plaindrome")

# tup1=('c','a','c','b','a','a')
# print(tup1.count('a'))

# list=[1,4,3,2,8,5,9,6]
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)



#Dictionaries and Sets
#dictionary is a buuilt in data type that stores the data in the form of key value pair

# dict={
#     'name':'ram',
#     'age':23,
#     'marks':[2,34,65,2],
#     'weight':56.5,
#     'isAdult':True,
#     'color':('red','green','blue')

#     }
# print(dict)
# print(type(dict))
# print(dict['name'])
# print(dict['marks'])

# dict['age']=35
# dict['surname']='kg'
# print(dict)


#Nested Dictionary

# stud={
#     'name':'ram',
#     'marks':{
#         'math':90,
#         'science':83,
#         'eng':80
#     },
#     'age':23

# }

# print(stud)
# print(stud['marks'])
# print(stud['marks']['science'])
# print(type(stud))

#methods in the dictionary
# dict={
#     'name':'madhu',
#      'age':23,
#      'roll':34,
#      'marks':[23,45,67,89]
# }

# print(list(dict.keys()))
# print(list(dict.values()))
# print(list(dict.items()))
# print(dict.get('name'))
# dict.update({'age':25 ,'role':'student'})
# print(dict)

#sets: built in datatype that stores the collection of items in no particular order
#each element in the set is unique and immutable

# fit={1,2,3,'ram','sita',3,4,2,2,10}
# print(fit)
# print(type(fit))
# print(len(fit))

# set=set()#empty set
# dict={} #empty dictionary
# print(type(set))
# print(type(dict))


#set methods
# set={1,2,3,4,5}
# print(set)
# set.add(6)
# print(set)
# set.remove(1)
# print(set)
# set.pop()
# print(set)
# set.clear()
# print(set)

# set1={1,2,3,4}
# set2={2,3,5,6}
# print(set1.union(set2))
# print(set1.intersection(set2))


# dict={
#     'table':['a peice of furnitute','list of facts and figures'],
#     'act': 'a small animal'
# }
# print(type(dict))
# print(dict['table'][1])

# sub={'math','science','eng','social','science','math','eng'}
# print(len(sub))


# sub1=int(input('enter marks of first subject:'))
# sub2=int(input('enter:'))
# sub3=int(input('enter:'))
# marks={

# }
# marks.update({'math':sub1})
# marks.update({'eng':sub2})
# marks.update({'science':sub3})
# print(marks)


# set={9,'9.0'}
# print(set)

# set={('float',9.0),('int',9)}
# print(set)