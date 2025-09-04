num=int(input("Enter a number"))
if num == 0:
    count = 1
else:
    count=0
while n >0:
    n //=10
    count += 1
print("number of digits in", num, "is",count)