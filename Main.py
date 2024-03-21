from turtle import *

def EquilateralTest(S1, S2, S3):
    if S1 == S2 == S3:
        print("\n")
        print("You have an equilateral triangle")
        print("\n")
        TriangleType = "Equilatera"

def IsoscelesTest(S1, S2, S3):
    if S1 == S2 != S3 or S1 == S3 != S2 or S2 == S3 != S1:
        print("\n")
        print("You have an isosceles triangle")
        print("\n")
        TriangleType = "Isosceles"

def ScaleneTest(S1, S2, S3):
    if S1 != S2 != S3:
        print("\n")
        print("You have an scalene triangle")
        print("\n")
        TriangleType = "Scalene"

def RightAngleTest(S1, S2, S3):
    if  S1 ** 2 == S2 ** 2 + S3 ** 2:
        print("\n")
        print("You have an Right angle triangle")
        print("\n")
        TriangleType = "Right Angle"

def DrawTriangle():
    print()

#Main Program
print("\n")
print("\n")
print("Welcom to the Triangle Idetification Program")
print("\n")
print("Writen by D Styles 2024 \n")



NewTriangle = True

while NewTriangle == True:
    side1 = int(input("Please enter the length for Side 1 of your triangle (this should be your longest side)"))
    side2 = int(input("Please enter the length for Side 2 of your triangle "))
    side3 = int(input("Please enter the length for Side 3 of your triangle "))

    EquilateralTest(side1, side2, side3)
    IsoscelesTest(side1, side2, side3)
    ScaleneTest(side1, side2, side3)
    RightAngleTest(side1, side2, side3)

    MainMenuChoice = input("Would you like to test another Triangle? Y/N  ")
    print("\n")
    MainMenuChoice = MainMenuChoice.upper()
    if MainMenuChoice != "Y":
        print("Thank your for using this software")
        NewTriangle = False


# Open function to open the file "MyFile1.txt"  
# (same directory) in read mode and 
#file1 = open("Sides.txt", "r+") 
#print(file1.read())

#file1.write(str(side1) + ", " + str(side2) + str(side3) +"\n")
#file1.close()

#file1 = open("Sides.txt", 'r')
#Lines = file1.readlines()
 
#count = 0
# Strips the newline character
#for line in Lines:
#    count += 1
#    print("Line{}: {}".format(count, line.strip()))
