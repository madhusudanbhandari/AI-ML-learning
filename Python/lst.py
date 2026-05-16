# temperatures=[45,23,13,53,23]

# total=0

# for temp in temperatures:
#     total+=temp

# avg=total/len(temperatures)

# print(avg)


# import numpy as np
# temperatures=np.array([45,23,13,53,23])

# print(np.average(temperatures))

# prices=[100,200,300]
# disc_prices=[]

# for price in prices:
#     disc_prices.append(price-((price*10)/100))

# print(disc_prices)
    

##list comprehension

list1=[1,2,3]
list2=[3,4,5]

result=[x+y for x,y in zip(list1,list2)]

print(result)