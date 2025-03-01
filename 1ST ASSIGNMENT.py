#Author: Dwit panchal
#Date Due: Feb 28, 2025
#Description: Phyton basics coding assignment

import math

'''
VARIABLES 
'''
I = 2; """Assigns I as 2 - Integer"""
S = "blue, green and red"; """String"""
B = True; """Boolean"""
F = 1.01; """loat/double"""
C = "A"; """Char"""

print("Examples of types of variables:")
print() #leaves a blank space to help with organization and better user expereince as it makes it look clean

print("An example of an integer is", I)
print("An example of a string is", str(S))
print("An example of boolean is", B)
print("An example of float and a double is", F)
print("An example of char is", C)
print()
print()

print("Math equations:")
print()

addition = 2+9 #Does the equation 2+9
print("Example of addition: 2+2 =",addition)

subtraction = 11-9 #Does the equation 11-9
print("Example of subtraction: 1-9 =", subtraction)

multiplication = 2*8 #Does the multiplication 2x8
print("Example of multiplication: 2x8 =", multiplication)

division = 4/2 #Does the divison 4/2
print("Example of division: 4/2 =",division)

division_f = 400.00/200.9 #Does the devision and gives specific decimal points
print("Example of division with floats/double: 400.00/200.05 =", division_f)

root = math.sqrt(9) #Finds the square root of 9
print ("Example of square root: the square root of 9 is", root)

exponent = 2**2 #Squares the nummber before **, which in this case is 2
print("Example of squared: 2^2 =", exponent)

rem_1 = 24%6 #Finds the modulus 
print("Example of modulus is: 23%6 =", rem_1)
print()
print()



print("Lets use the quadratic formula!!")
print()

print("Write your a value and then press the enter key.")
a_value = float(input()) #Lets the user input a number of their choice. Float gives it ability to have decimals
print("Write your b balue and then press the enter key")
b_value = float(input())
print("Write your c value and then press the enter key")
c_value = float(input())

b1 = b_value**2
a1 = a_value*4
c1 = a1*c_value
ans1 = b1-c1 #Gets the final answer by subtracting the values b1-c1

print("The answer to the eqaution b^2-4ac using you values is", ans1)   
print()
print()

print("Lets find the volume of a cube, sphere, cone, cylinder with values of your choice")

print("Write a value for the length of the cube.")
Cube_val = float(input())
V_cube = Cube_val**3
print("The volume of a cube with your given length is", V_cube)
print()

print("Write a value for the radius of sphere")
Sphere_val_rad = float(input())
V_sphere = 4/3*math.pi*Sphere_val_rad**3 #perfoms the equation 4/3x3.14xr^3
print("The volume of a sphere with your given radius is", V_sphere)
print()

print("Write a value for the radius of the cone")
Cone_val_rad = float(input()) #Lets the user pick a value for the radius
print("Write a value for the height of the cone")
Cone_val_height = float(input()) #LEts the user pick a value for height
V_cone = 1/3*math.pi*Cone_val_rad**2*Cone_val_height
print("The volume of a cone with your given radius and height is", V_cone)
print()

print("Write a value for the radius of the cylinder")
Cyl_val_rad = float (input())
print("Write a value for the height of the cyclinder")
Cyl_val_height = float(input())
V_cyl = math.pi*Cyl_val_rad**2*Cyl_val_height
print("The volume of a cylinder with your given radius and height is", V_cyl)