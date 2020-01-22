s1 = int(input("Input a side length"))
s2 = int(input("Input a side length"))
s3 = int(input("Input a side length"))
hyp = 0
l1 = 0
l2 = 0
if s1+s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print("This can make a triangle")
    if s3 >= s1 and s3 >= s2:
        print(s3, "is the hypotenuse, and {}, {} are the legs".format(s1, s2))
        hyp = s3
        l1 = s1
        l2 = s2
    elif s2 >= s3 and s2 >= s1:
        print(s2, "is the hypotenuse, and {}, {} are the legs".format(s1, s3))
        hyp = s2
        l1 = s1
        l2 = s3
    elif s1 >= s2 and s1 >= s3:
        print(s1, "is the hypotenuse, and {}, {} are the legs".format(s3, s2))
        hyp = s1
        l1 = s2
        l2 = s3
    else:
        print("There is no definitive hypotenuse")
    if hyp * hyp == l1*l1 + l2*l2:
        print("This is an right triangle")
    elif hyp * hyp > l1 * l1 + l2 * l2:
        print("This is an obtuse triangle")
    elif hyp * hyp < l1 * l1 + l2 * l2:
        print("This is an acute triangle")
else:
    print("Those sides do not make a valid triangle.")

















































































































