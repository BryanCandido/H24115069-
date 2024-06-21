num = input("Input an integer number:")
if num.isdigit():
    num = int(num)
    n1 = 0
    n2 = 1
    for i in range(1,num+1):
        n1, n2 = n2, n1 + n2
    print("The %d-th Fibonacci sequence number is:"%(num), n1)