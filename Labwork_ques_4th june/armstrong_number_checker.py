num = int(input("Enter a number: "))
temp = num
power = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
