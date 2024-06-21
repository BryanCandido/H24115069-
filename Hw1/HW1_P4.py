#Problem 4
h = int(input("Input the height of the 1st ball: "))
m1 = int(input("Input the mass of the 1st ball: "))
m2 = int(input("Input the mass of the 2nd ball: "))

g = 9.8
v=(2*g*h)**0.5
U1 = m1*g*h
U2 = m2*g*h
print("The velocity of the 1st ball after slide:" , v)

v2f=(2*m1*v)/(m1+m2)
print("The velocity of the 2nd ball after collision:" ,v2f)

#input the height, mass of the first and second ball, labelled by h, m1, and m2
#Make sure that only integers are inputted with the function int and function input used for inputting the values
#enter the formula of potential energy, U=𝑚∙𝑔∙ℎ, there are 2 potential energy since there are 2 balls colliding
#Enter the formula for the final velocity from the kinetic energy
#use * for multiplication and ** for power
#Finally, use the code print to show the final result of calculation of velocity for first and second ball