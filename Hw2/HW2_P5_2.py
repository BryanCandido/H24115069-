str_ = input("Enter a string:")
count = len(str_)
x = 0
y = 0
for i in range(count):
     left = right = i
     while left >= 0 and right < count and str_[left] == str_[right]:
         if right - left + 1 > y:
             y = right - left + 1
             x = left
         left -= 1
         right += 1
     left = i
     right = i + 1
     while left >= 0 and right < count and str_[left] == str_[right]:
         if right - left + 1 > y:
             y = right - left + 1
             x = left
         left -= 1
         right += 1
print(str_[x:x+y])
