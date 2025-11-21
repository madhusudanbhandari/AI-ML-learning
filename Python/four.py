#class and objects

#class@ classs is a blueprint for creating objects
# class students:
#     name='madhu'

# s1=students()
# print('your name is',s1.name)
# s2=students()
# print(s2.name)

###Constructor
#all the classes have the function __init__() which is alwas executed when the object is being inititalized

# class students():
#    #name='madhu'
#    def __init__(self,fullname):
#       print(fullname)

# s1=students('madhu')


# class students():
#     def __init__(self,fullname):
#         self.name=fullname

# s1=students('madhu')
# print(s1.name)
# #self is the parameter which is a reference to the current instances of class , and is used to access variables that belongs to the class



# class students():
#     #default constructor
#     clg_name='ncit'         #class attribute
#     def __init__(self):
#         pass
    
#     #parameterized constructor ,the one with which the parameters passed as arguments match gets executed
#     def __init__(self,name,marks):
#         self.name=name                  #####instance attribute
#         self.marks=marks

# s1=students('ram',45)
# print(s1.name,s1.marks,s1.clg_name)
# print(s1.name,s1.marks,students.clg_name)


###class and instance attributes 
#class attribute: common for all the instances of the classs
#instance attribute: different for all the instances of the class

#when there are both class and instance attributes with the same name then the precedence of the obj or instance attr is higher than class attribute


############Methods: methods are basically the functions that belongs to objects

# class students():  ###class
#     def __init__(self,name,marks):  ###constructor
#         self.name=name
#         self.marks=marks

#     def welcome(self):      ##method 1
#         print('welcome',self.name)

#     def get_mark(self):   ##method 2
#         print('your marks are',self.marks)

# s1=students('madhu',45)
# print(s1.name)
# s1.welcome()
# s1.get_mark()

##create student class that takes name and marks of 3 students as the argument in the constructor .then create a method to print the average

# class students():
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name=name
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3
        
#     def average(self):
#         avg=((self.marks1+self.marks2+self.marks3)/3)
#         print(avg)

# s1=students('ram',34,45,23)
# print(s1.name)
# s1.average()


####static methods
#the static methods are the methods that dont use self parameter:  static  methods are basically used at the class level

# class student:
#     def __init__(self):
#         pass
#     @staticmethod ##decorator
#     def college():
#         print("ncit")

# s1=student
# s1.college()


###Encapsulation and 'Abstraction
#Abstraction:hiding the implementationn details and only showing the essential features

# class car:
#     def __init__(self):
#         self.acc=False
#         self.clutch=False

#     def start(self):
#         self.acc=True
#         self.clutch=True
#         print('car started')
# c1=car()
# c1.start()

###encapsulation  ::wrapping data and functions into the single unit (object)


###create a account class with 2 attributesbalance and accno create method for debt credit &printing the balance


# class account:
#     def __init__(self,bal,acc):
#         self.bal=bal
#         self.acc=acc

#     def debit(self,amount):
#         self.bal+=amount
#         print('rupees',self.bal,'debitted in your account no',self.acc)
        
#     def credit(self,amount):
#         self.bal-=amount
#         print('rupees',self.bal,'credited from your account no',self.acc)
        
# acc1=account(1000,24556347567238)
# acc1.debit(1000)
# acc1.credit(500)


####del keyword:used to delete the properties if the object or the object itself
# class stud:
#     def __init__(self,name):
#         self.name=name
    
# s1=stud('madhu')
# del s1.name
# print(s1.name)
# del s1
# print(s1.name)

#private like attrubutes
#private attributes are only meant to be used only within the class and are not accessible from outside

# class student:
#     # def __init__ (self,name):
#         _name='madhu'

#         def _name(self):
#         # self.name='madhu'
#         # print(self.name)
#          print('hello')
 
#         def na(self):
#          self._name()

    
# s1=student()
# #print(s1.name)
# s1.na()


###########Inheritence:when one class inherits or serives the properties and methods of the another claass(parent/base)
###single level inheritence
# class car:
#     @staticmethod
#     def start():
#         print('car started')

#     @staticmethod
#     def stop():
#         print('car stopped')

# class tata(car):
#     def __init__(self,name):
#         self.name=name

# car1=tata('suv')
# print(car1.name)
# car1.start()   ###tata car inherited the properties of the class car 




###multilevel inheritence       
# class car:
#     @staticmethod
#     def start():
#         print('car started')
    
#     @staticmethod
#     def stop():
#         print('car ended')
        
# class brand(car):
#     def __init__(self,name):
#         self.name=name

# class name(brand):
#     def __init__(self,name,model):
#         super().__init__(name)
#         self.model=model

# car1=name('ferrari',2025)
# print(car1.model)
# print(car1.name)
# car1.start()



######multiple inheritence
# class car:
#     def __init__(self,date):
#         self.date=date

# class brand:
#     def __init__(self,type):
#         self.type=type

# class name(car,brand):
#     def __init__(self,date,type,model):
#         car.__init__(self,date)
#         brand.__init__(self,type)
#         self.model=model

# n1=name(2025,'diesel',34)
# print(n1.date)
# print(n1.model)
# print(n1.type)


####super method::::::super is the method which is used to access the methods of the parent classs

# class car:
#     def __init__(self,name):
#         self.name=name

# class brand(car):
#     def  __init__(self,name,type):
#         super().__init__(name)
#         self.type=type

# car1=brand('toyota','diesiel')
# print(car1.type)
# print(car1.name)


###class method
# class person:
#     name='abcd'

#     @classmethod
#     def changeName(cls,name):
#         cls.name=name

# p1=person()
# p1.changeName('ram')
# print(p1.name)
# print(person.name)

###property decorator
# class student:
#     def __init__(self,math,phy,chem):
#         self.math=math
#         self.phy=phy
#         self.chem=chem

#     @property   ####used to use method as the property
#     def changeper(self):
#        return str((self.math+self.phy+self.chem)/3)+'%'

# s1=student(56,34,67)
# print(s1.changeper)
# s1.phy=60
# print(s1.phy)
# print(s1.changeper)
        
 

#####Polymorphismmm : when the same operator is allowed to have  different meaning according to the context

# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def shownumber(self):
#         print(self.real,'i+',self.img,'j')


#     def __add__(self,num2):  ##__add__ is a dunder function
#         newreal=self.real+num2.real
#         newimg=self.img+num2.img
#         return complex(newreal,newimg)


# num1=complex(3,5)
# num1.shownumber()

# num2=complex(5,6)
# num2.shownumber()

# num3=num1+num2
# num3.shownumber()
   
##question:define a circle class to createa a circle with radius r using constructor.
#define an area() method of the class which calculates the area of circle.
#define a perimeter() method of the class which allows you to  calculate the perimeter of circle


# class circle:
#     def __init__(self,r):
#         self.r=r

#     def Area(self):
#         area=3.14*(self.r)**2
#         #return circle(area)
#         print (area)
     
#     def Peri(self):
#         perimeter=2*3.14*self.r
#         #return circle(perimeter)
#         print(perimeter)

# c1=circle(43)
# c1.Area()
# c1.Peri()



#q2
# class Employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary

#     def showDetails(self):
#         print(self.role,self.department,self.salary)

# class Engineer(Employee):
#     def __init__(self, role, department, salary,name,age):
#         super().__init__(role, department, salary)
#         self.name=name
#         self.age=age
    
#     def showDetails(self):
#         print(self.role,self.department,self.salary,self.name,self.age)

# e1=Engineer('eng','it',2400,'ram',34)
# e1.showDetails()



##q3
# class Order:
#     def __init__(self,items,price):
#         self.items=items
#         self.price=price

#     def __gt__(self,ord2):
#         # if(self.price>ord2.price):
#         #     print('order1>order2')
#         # else:
#         #     print('order2>order1')
#         return self.price>ord2.price
    

# ord1=Order('apple',95)
# ord2=Order('banana',67)
# print(ord1>ord2)

