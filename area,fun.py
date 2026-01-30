#write a py script to find the area and volume of the user given figure (cube,cubboid,sphere)

def area_figure(f):
	if f == "cube":
		s=int(input("enter the sides:"))
		area_of_cube=6*(s**2)
		volume_of_cube=s**3
		print("area_of_cube",area_of_cube)
		print("volume_of_cube",volume_of_cube)
	elif f =="cuboid":
		l=int(input("enter the length:"))
		b=int(input("enter the breadth:"))
		h=int(input("enter the height:"))
		area_of_cuboid=2*(lb+bh+hl)
		volume_of_cuboid=l*b*h
		print("area_of_cuboid",area_of_cuboid)
		print("volume_of_cuboid"<volume_of_cuboid)
	elif f== "sphere":
		r=int(input("enter the radius:"))
		area_of_sphere=4*(22/7)*(r**2)
		volume_of_sphere+(4/3)*(22/7)*(r**3)
		print("area_of_sphere",area_of_sphere)
		print("volume_of_sphere",volume_of_sphere)
	else:
		print("invalid syntax")
f=input("enter the figure:")
area_figure(f)
