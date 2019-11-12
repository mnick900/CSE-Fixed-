import math
# 1
First = input("First name:")
Last = input("Last name:")
print("Welcome", First + Last, "Nice to see you today!")
print()
# 2
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
print(address, ',', Street_name, ',', street_type)
print(city, ',', state, ',', zip_code)
# 4
print()
print("A=4, B=3, C=2, D=1, F=0  ")
class1 = int(input("Enter grade in numerical value shown above for your first class"))
class2 = int(input("Enter grade in numerical value shown above for your first class"))
class3 = int(input("Enter grade in numerical value shown above for your first class"))
class4 = int(input("Enter grade in numerical value shown above for your first class"))
class5 = int(input("Enter grade in numerical value shown above for your first class"))
class6 = int(input("Enter grade in numerical value shown above for your first class"))
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
# 7
print()
L = int(input("Length:"))
h = int(input("Height:"))
w = int(input("Width:"))
print("Volume =", L*h*w)
print("Surface area =", ((L*w)*2)*((L*h)*2)*((w*h)*2))
# 8
print()
radius = int(input("Radius:"))
height = int(input("Height:"))
print("Volume:", (3.14*(radius**2)*height))
print("Surface area =", 2*(3.14*(radius**2)*height)+(2*(3.14*(radius**2))))
# 9
print()
variable = int(input("x = "))
print("y=", (variable+2)*(variable+2))
print("y=", (variable+2)/(variable+2))
# 10
print()
a = int(input("Enter value of 'a' in a quadratic equation"))
b = int(input("Enter value of 'b' in a quadratic equation"))
c = int(input("Enter value of 'c' in a quadratic equation"))
d = (b**2)-(4*a*c)
print("Discriminant= ", (b**2)-(4*a*c))
print("First solution:"(-b+(d**(1/2)))/2*a)
print("Second solution:"(-b-(d**(1/2)))/2*a)









