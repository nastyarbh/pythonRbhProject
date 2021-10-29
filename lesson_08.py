num = input("enter number ")
num = str(num)
length = len(num)
sum = 0

for i in range(length):
    sum = sum + int(num[i])

print("Результат ", sum)
