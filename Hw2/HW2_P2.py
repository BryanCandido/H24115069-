ranges = input("Input the range number:")
print("\nPerfect number:")                                  
if ranges.isdigit():                                        
    for num in range(1, int(ranges) + 1):                   
        perfect_numbers = 0                                 
        for factors in range(1, num):                      
            if num % factors == 0:                        
                                                            
                perfect_numbers += factors                 
        if perfect_numbers == num:                          
            print(perfect_numbers)                          
else: print("Please input a whole number!")                