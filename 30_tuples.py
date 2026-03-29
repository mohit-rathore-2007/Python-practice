#Create an empty tuple
empty_tuple = ()
#or
empty_tuple = tuple()

#create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers = ("Shyam","Ram","Mohan")
sisters = ("Radha","Priya","Pooja")

#Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

#How many siblings do you have? count
total_siblings = len(siblings)
print("Total siblings are : ",total_siblings)


#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Vikas","Krishna")
print("total family members are : ", family_members)

#Unpack siblings and parents from family_members
siblings = family_members[:-2]
parents = family_members[-2:]
print("all the siblings : ",siblings)
print("Parents : ",parents)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
 
vegetables = ("Patato","cabbage","spinach")
fruits = ("banana","mango","orange")
animal_products = ("Milk","egg","Cheese")


food_stuff_tp = vegetables+fruits+animal_products
print("Food Stuff tuple : ",food_stuff_tp)


#Change the about food_stuff_tp tuple to a food_stuff_list list
food_stuff_list = list(food_stuff_tp)
print("food stuff list: ",food_stuff_list)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_tp[4]
print("Middle item: ",middle_item)

#Slice out the first three items from food_staff_lt list
first_three = food_stuff_list[0:3]
print("first three items: ",first_three)

#Slice out the last three items from food_staff_lt list
last_three = food_stuff_list[-3:]          #(agar -1 bhi lenge to vo ek kam chalega)
print("Last three items: ",last_three)

#Delete the food_staff_tp tuple completely
del food_stuff_tp
print("Deleted food_stuff_tp succesfully")


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

#Check if 'Estonia' exists in nordic countries
is_present = "Estonia"
print(is_present in nordic_countries)

#Check if 'Iceland exists in nordic countries
is_present = "Iceland"
print(is_present in nordic_countries)



