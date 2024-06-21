#Problem 3_2
n = input('Input polynomial: ')
x = int(input('Input the value of X: '))

list = []
start = 0
total = 0

for index, sym in enumerate(n): 
    if sym == '+' or sym == '-' or sym == '*' or sym == '^':
        m = n[start:index]
        list.append(m)
        list.append(sym)
        start = index + 1
    if index == len(n) - 1:
        m = n[start:]
        list.append(m)

for index, value in enumerate(list): 
    if value == 'X':
        list[index] = x
    if value.isdigit():
        list[index] = int(value)

for index, value in enumerate(list): 
    if value == '^':
        result = list[index-1] ** list[index+1]
        list[index] = result
        del list[index+1]
        del list[index-1]

for index, value in enumerate(list): 
    if value == '*':
        result = list[index-1] * list[index+1]
        list[index] = result
        del list[index+1]
        del list[index-1]

for index, value in enumerate(list): 
    if value == "-":
        total -= list[index+1]
        del list[index+1]
    elif value == "+":
        total += list[index+1]
        del list[index+1]
    elif list[0] != "":
        total += value

print ("Evaluated Result: ", total)









    