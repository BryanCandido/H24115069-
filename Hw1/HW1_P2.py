#Problem 2
f = int(input("Input the force: "))
("force = ", f)

m1 = int(input("Input the mass of m1: "))
("Input the mass of m1 =", m1)

d = int(input("Input the distance: "))
("Input the distance =", d)

G = 6.67*(10**-11)
m2 = (f*(d**2)/(G*m1))

c = 299792458 
En = (float(m2)*(c**2))
print ("the mass of m2 =",m2)

print("the energy of En=",En)

#input the force, mass of m1, and distance, labeled by f, m1, and d
#only integers are inputted with the function int and function input used for inputting the values
#the formula of gravity, use * for multiplication and ** for power
#The code float is used to convert the value into a decimal or fractional value from integers
#Finally, use the code print to show the final result of calculation using the formula to get the values of m2 and energy of the second object