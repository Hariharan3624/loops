word = input("please enter your word: ")
char = input("please type in your letter:")
a = 0
count = 0
while(a < len(word)):
    if(word[a] == char):
        count = count + 1
    a = a + 1
print("the total nember of times", char,"has occured is", count)