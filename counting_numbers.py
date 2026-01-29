num = int(input("enter a number: "))
count = 0
while num!=0:
   num //= 10
   count += 1
print ("the count of the figures in your number is",count)