num = input("The number of the requested element in Fibonacci (n)= ")
n1 = 0
if num.isdigit():
    n1 = 0
    n2 = 1
    num = int(num)
    for i in range(1,num+1):
        n1, n2 = n2, n1 + n2
else:
    print("Please input a non-decimal number!")
n = n1

S = input("The first string for palindromic detection (s1) = ").lower()
S1 = input("The second string for palindromic detection (s2) = ").lower()
count = len(S)
count1 = len(S1)
max_ = 0
sub = ""
for i in range(count):
    for x in range(i+1, count+1):
        str_ = S[i:x]
        if str_ == str_[::-1] and len(str_) > max_:
            max_ = len(str_)
            sub = str_

max2_ = 0
sub2 = ""
for i in range(count1):
    for x in range(i+1, count1+1):
        str2_ = S1[i:x]
        if str2_ == str2_[::-1] and len(str2_) > max2_:
            max2_ = len(str2_)
            sub2 = str2_

s1 = len(sub)
s2 = len(sub2)
mes = input("The plaintext to be encrypted:")
print("----- extract key for encrypt method -----")
print("The %d-th Fibonacci sequence number is:"%(num), n)
print("Longest palindrome substring within the first string is:", sub)
print("Length is:", s1)
print("Longest palindrome substring within the second string is:", sub2)
print("Length is:", s2)
print("----- encryption completed -----")
mes = mes.strip()
mes2 = ""
for char in mes:
    cc = ord(char) + n
    ac = cc*s1 + s2
    if ac > 90:
        ac = ((ac-65)%26)+65
    if ac < 90:
        ac = ac
    enc = chr(ac)
    mes2 += enc
print("The encrypted text is:", mes2)
