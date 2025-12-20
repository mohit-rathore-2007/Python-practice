'''1.write python script to find area of circle 
  2.write python script to determine ice cream requirement making 
	  1000 cone of ice where dimension of the cone are user defined 
	  and ice cream is filled only till top of the cone
  3.write a python script to identify the dimensions of the box 
      required to pack 12 piece of the cone ice cream where the box can square or rectangle 
      whatever which lower material required 
'''

#1----
'''Radius = int(input("Enter the Radius : "))
area_of_circle = (22/7*Radius*Radius)
print("Area of Circle : ",area_of_circle)
'''

#2----
'''print("=== Ice Cream Requirement Calculator ===")

r=float(input("Enter the radius : "))
h=float(input("Enter the height : "))

volume_cone = (1/3) * (22/7) * r * r * h

total_volume = 1000 * volume_cone

total_volume_liters = total_volume / 1000


print("Total icecream requirement of 1000 cone : ",round(total_volume) , "Liters")
'''

#3----

r = float(input("Enter the radius of the cone : "))
h = float(input("Enter the height of the cone : "))

S = 4 * (2*r)
H_square = h
SA_square = 2 * (S**2 + 2 * S * H_square)



L_rect = 4 * (2*r)
W_rect = 3 * (2*r)
H_rect = h
SA_rect = 2 *(L_rect*W_rect + L_rect*H_rect + W_rect*H_rect)

print("Surface area of square box : ",SA_square,"cm")
print("Surface area of rectangle box : ",SA_rect,"cm")
print("=============================================")
if SA_square < SA_rect:
	print("Square box required lower material")
else:
	print("Rectangle box required lower material")



