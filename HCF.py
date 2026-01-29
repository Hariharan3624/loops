num1 = float(input("please type in one of the number you want to find the HCF of: "))
num2 = float(input("please type in the other number you want to find the HCF of: "))
while(num2 != 0):
    temp = num2
    num2 = num1 % num2
    num1 = temp
hcf = num1
print("HCF of this two numbers is",hcf)