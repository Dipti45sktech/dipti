n = int(input("Enter a number:"))
sum = 0
prod = 1
temp = n
while temp > 0:
    d = temp % 10
    sum += d
    prod *= d
    temp = temp // 10
if sum == prod:
    print("Spy number")
else:
    print("Not a Spy number")

