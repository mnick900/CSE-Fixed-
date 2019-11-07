import math
#1
First = input("First name:")
Last = input("Last name:")
print("Welcome", First + Last, "Nice to see you today!")
print()
#2
hour = input("Hour:")
minute = input("Minute:")
AMPM = input("AM or PM?")
print(hour, ":", minute, "", AMPM)
# 3
print()
Name = input("Full name:")
address = input("Input address:")
Street_name = input("street name:")
street_type = input("Street type:")
city = input("City:")
state = input("State:")
zip_code = input("Zip code:")
print(Name)
print(address+Street_name+street_type)
print(city, ',', state, ',', zip_code)
# 4
print()
class1 = 1
class2 = 4
class3 = 3
class4 = 3
class5 = 4
class6 = 4
print("gpa:", (class1+class2+class3+class4+class5+class6)/6)
# 5
print()
length = int(input("Length:"))
width = int(input("Width:"))
print("area= ", length*width)
print("perimeter= ", (length*2)+(width*2))
# 6
print()
l1 = int(input("First side length:"))
l2 = int(input("Second side length:"))
l3 = int(l1 + l2)
print("Hypotenuse =", math.sqrt(l3))
print("Perimeter =", (l1+l2+(math.sqrt(l3))))
print()
l = int(input("Length:"))
h = int(input("Height:"))
w = int(input("Width:"))
print("Volume =", l*h*w)
print("Surface area =", ((l*w)*2)*((l*h)*2)*((w*h)*2))
print()
radius = int(input("Radius:"))
height = int(input("Height:"))
print("Volume:", (3.14*(radius**2)*height))
print("Surface area =", 2*(3.14*(radius**2)*height)+(2*(3.14*(radius**2))))















