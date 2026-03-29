
#Add one item 
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

#Add multiple items using update() 
#The update() allows to add multiple items to a set. The update() takes a list argument.

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.update(["papaya","cherry"])
print(fruits)

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle'}

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print("Added: ",it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(["Amazon","Meta","Deloitte"])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove("Meta")
print(it_companies)

#level 2
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}

#Join a and b
# both can be used but union will return a new set and update will add in the existing set

'''a.union(b)
print(a)'''

'''a.update(b)
print(a)

#Find a intersection b

a.intersection(b)
print("Intersection: ",a)

#Is a subset of b
a.issubset(b)
print(a)'''

#Are a and b disjoint sets

'''a.disjoint(b)
print(a)
'''
#Join A with B and B with A
a.update(b)
print("A joined with B: ",a)

#now B with A 
BA = b.union(a)
print("B joined with A",BA)

#What is the symmetric difference between A and B
a.symmetric_difference(b)
print(a)

#Delete the sets completely
del BA
#print(BA)
print("Set deleted succesfully")

age = [22, 19, 24, 25, 26, 24, 25, 24]
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?

st = set(age)
print("Converted to set: ",st)

print("The length of list:",len(age))
print("The length of set:",len(st))

