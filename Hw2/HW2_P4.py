layers = input("Enter the number of layers (2 to 5) = ")            #lets users input the desired values
sides = input("Enter the side length of the top layer = ")
growth = input("Enter the growth of each layer = ")
width = input("Enter the trunk width (odd number, 3 to 9) = ")
height = input("Enter the trunk height (4 to 10) = ")
if layers.isdigit() and sides.isdigit() and height.isdigit() and growth.isdigit() and width.isdigit():  
    layers = int(layers)    
    sides = int(sides)
    growth = int(growth)
    width = int(width)
    height = int(height)
    if 2 <= layers <= 5 and 4 <= height <= 10 and width / 2 != 0 and 3 <= width <= 9:   
        base_formula = (2 * ((sides-1) + (layers - 1) * growth) + 1)    
        top = " "*(base_formula//2)+"#"     
        print(top)
        for x in range(1, layers + 1):      
            for i in range(1,sides+growth*(x-1)-1): 
                mid = " " * (base_formula // 2 - i) + "#" + "@" * (i + (i - 1)) + "#" 
                print(mid)
            base = " " * (base_formula//2-(sides-1)-growth*(x-1)) + "#" * (2 * (sides + (x - 1) * growth) - 1)  
            print(base)
        for x in range(1, height+1):  
            trunk = " "*(base_formula//2 - width//2) + "|"*width 
            print(trunk)
