print("half pyramid pattern of stars(*):")
n = int(input("enter the number of rows: "))
print("normal right triangle star pattern")
for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()

print("Mirrored Right Triangle Star Pattern") 
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if(j <= n - i):
            print(' ', end = ' ')
        else:
            print('*', end = ' ')
    print()