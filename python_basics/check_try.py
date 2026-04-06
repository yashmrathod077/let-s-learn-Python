side1 = int(input("enter the first side  :"))
side2 = int(input(" enter the second side :"))
side3 = int(input(" enter the third side :"))

if side3 == side1 + side2 or side2 == side1 + side3 or side3 == side1 + side2:
    print("it cant creat a triangle ")
elif side2 == side1 and side1 == side3:
    print("it is a  equilateral triangle ")
elif side2 != side1 and side2 != side3:
    print("it is a scalene triangle  ")
else:
    print(" it is an  isosceles triangle  ")
