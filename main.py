import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number=random.randint(1,100)
print(number)
diff=input("Choose a difficulty. Type 'easy' or 'hard':")
if(diff=="easy"):
    n=10
elif(diff=="hard"):
    n=5
for i in range(0,n+1):
    m=n-i
    if(m==0):
        print("Out of guesses")
    else:
        print(f"You have {m} attempts remaining to guess the number.")
        guess=int(input("Make a guess:"))
        if (guess<number):
            print("Too Low")
        elif(guess>number):
            print("Too High")
        else:
            print("Correct")
            break
