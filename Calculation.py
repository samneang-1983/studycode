# num = int (input ("Enter Number"))
# result = num*num
# print("Square number of ",num, "is", result)
#### Square ####
name = "----------Area of the square----------"
print(name)
d1 = (int(input("Enter your first number: ")))
d2 = (int(input("Enter your second number: ")))
area_square = d1 * d2
if d1 <= 0 or d2 <= 0:
    print ("Please enter a positive number")
elif d1 > d2:
        print ("The first number is greater than the second number")
elif d1 < d2:
        print ("The second number is greater than the first number")
elif d1 == d2:
        print ("Area of the square is: ", area_square)
else:
        print ("Please enter a valid number")


#### Rectangle ####  
name = "-----------Area of the rectangle-----------"
print(name) 
d1 = (int(input("Enter your length number: ")))
d2 = (int(input("Enter your width number: ")))
area_Rectangle = d1 * d2
if d1 <= 0 or d2 <= 0:
    print ("Please enter a positive number")
elif d1 > d2:
        print ("Area of the rectangle is: ", area_Rectangle)
elif d1 < d2:
        print ("The width is can not be greater than the length")
elif d1 == d2:
        print ("The length is can not be equal to the width")
else:
        print ("Please enter a valid number")


#### Rhombus ####
name = "-----------Area of the rhombus Using Diagonals-----------"
print(name)
d1 = (int(input("Enter your p number: ")))
d2 = (int(input("Enter your q number: ")))
area_Rhombus = d1*d2/2
if d1 < 0 or d2 < 0:
    print ("Please enter a positive number")
elif d1 == 0 or d2 == 0:
    print ("It can not be zero")
else:
    print ("Area of the rhombus is: ", area_Rhombus)


#### Parallelogram ####
name = "-----------Area of the parallelogram-----------"
print(name)
d1 = (int(input("Enter your Base number: ")))
d2 = (int(input("Enter your Height number: ")))
area_Parallelogram = d1 * d2
if d1 < 0 or d2 < 0:
    print ("Please enter a positive number")
elif d1 == 0 or d2 == 0:
    print ("It cannot be zero")
else:
    print ("Area of the parallelogram is: ", area_Parallelogram)



#### Triangle ####
name = "-----------Area of the triangle-----------"
print(name)
d1 = (int(input("Enter your base number: ")))
d2 = (int(input("Enter your height number: ")))
area_Triangle =  d1 * d2 / 2
if d1 < 0 or d2 < 0:
    print ("Please enter a positive number")
elif d1 == 0 or d2 == 0:
    print ("It cannot be zero")
else:
    print ("Area of the triangle is: ", area_Triangle)



#### Circle ####
name = "-----------Area of the circle-----------"
print(name)
d1 = (int(input("Enter your radius: ")))
d2 = 3.14
area_Circle = d2 * d1 * d1
if d1 < 0:
    print ("Please enter a positive number")
elif d1 == 0:
    print ("It cannot be zero")
else:
    print ("Area of the circle is: ", area_Circle)