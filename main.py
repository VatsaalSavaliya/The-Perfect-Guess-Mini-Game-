import random  
n = random.randint(0,100)
a = -1
guesses = 1
while(a != n):
    a = int(input("guess the number: "))
    if (a>n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higer number please")
        guesses +=1
    
print(f"You have guessed the {n} number correctly in {guesses} attempt")
