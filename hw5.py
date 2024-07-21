import random 
#Section 1
pos = 0
neg = 0
neut = 0
sev = 0
lastPos = 0
lastNeg = 0
num = 0
for i in range(10):
    num = int(input("Write a number"))
    if num == -9999:
        break
    elif num == 1000 or num ==-1000:
        continue
    elif num > 0:
         pos += 1
         lastPos = num    
    elif num < 0:
         neg += 1
         lastNeg = num
    elif num == 0:
         neut += 1
    elif num % 7 == 0:
         sev += 1
if lastPos == 0:
    lastPos = "None"
if lastNeg == 0:
    lastNeg = "None"
if num != -9999:
    print(f"Positives {pos}, Negatives {neg}, Zeroes {neut}, divisible by 7 {sev}, Last positive number {lastPos}, Last negative number {lastNeg}")    
    
#Section 2

conStr = "yes"
tries = int(1)
num = int(0)
game = True 
while game:
    tries = int(1)
    rand = random.randint(1,100)
    print("Welcome to the guessing game !")
    num = int(input("Guess the random number!"))            
    if num == rand:
        Print(f"Bingo! {tries} Tries")
        conStr = input("Do you want to play again ?")
        if conStr == "no":
            break            
        else:        
             continue           
    else:
        while True:
            if tries != 1:
                num = int(input("Guess the random number!"))    
            tries += 1
            if num > rand:
                print("The random number is smaller than that")
                continue
            elif num < rand:
                print("The random number is bigger than that")
                continue
            else:
                print(f"Bingo! {tries} Tries")
                conStr = input("Do you want to play again ?")
                if conStr == "no":
                    game = False
                    break
                else:
                    break

#Section 3
num = int(input("Enter a number"))
i = int(1)
x = 0
prnt = int(1)
while i < num + 1:
    while x < i:
        print(prnt, end=' ')
        x += 1                                          
        prnt += 1
    i += 1                                               
    prnt = 1
    x = 0
    print("")
i = num - 1
while i > 0:
    while x < i:
        print(prnt, end=' ')
        x += 1
        prnt += 1
    i -= 1
    prnt = 1
    x = 0
    print("")  
    
num = int(input("Enter a number"))
while num % 2 == 0:
    num = int(input("Enter an odd number"))
spacer = num // 2
i = 1
while i < num+1:
    print(' ' * spacer+"*" * i)
    i += 2
    spacer -= 1                                                                                                                                                                                                                                                                                                                                                                                                                                                           