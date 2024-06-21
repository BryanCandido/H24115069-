#Problem 3
V = int(input("Input Velocity: "))
c = 299792458

gamma = 1 / (1-(V**2/c**2))**0.5
s = float(V/c)
Alpha = 4.3 
Barnard = 6.0 
Betelgeuse = 309 
Andromeda  = 2000000 

alpha_t = (Alpha/gamma)
bernard_t = (Barnard/gamma)
betelgeuse_t = (Betelgeuse/gamma)
Andromeda_t = (Andromeda/gamma)

print("Percentage of Light speed=",s)
print("Travel time to Alpha Centauri=",alpha_t)
print("Travel time to Barnard's Star=",bernard_t)
print("Travel time to Betelgeuse (in the Milky Way)=",betelgeuse_t)
print("Travel time to Andromeda Galaxy (closest galaxy)=",Andromeda_t)

#input the velocity labeled by v, whereas c is a known value as the speed of light
#Make sure that only integers are inputted with the function int and function input used for inputting the values
#enter the formula of Einstein's equation, here use * for multiplication and ** for power
#The code float is used to convert the value into a decimal or fractional value from integers
#calculate the time experienced by the astronauts, this shows the formula of time to the destination
#divided by the gamma, each one marked by an additional "_t"
#Finally, use the code print to show the final result of calculation using the formula to get the values of percentage