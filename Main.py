print("Hello World")
print("Testing online changes and effect on locally stored files")
print("Yet another line of code")
side1 = int(input("Side 1 Size"))
side2 = int(input("Side 2 Size"))
side3 = int(input("Side 3 Size"))
# Open function to open the file "MyFile1.txt"  
# (same directory) in read mode and 
file1 = open("Sides.txt", "r+") 
print(file1.read())

file1.write(str(side1) + ", " + str(side2) +"\n")
file1.close()

file1 = open("Sides.txt", 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
