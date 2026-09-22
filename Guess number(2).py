import random
number = random.randint(1, 100) 
attempts = 0
max_attempts = 7
print("Guessing game.")
print("I have choosen number number between 0 to 100 ")
while attempts < max_attempts:
    guess = int(input("ENTER YOUR GUESS:"))
    attempts += 1
    if guess < number:
        print("Too low. Try again!!")
    elif guess > number :
        print("Too High. Try again!!")
    else :
        print("correct!!")
        print("You guessed the number in" , attempts, "attempts.")
        break
    print("Chances left:" , max_attempts - attempts)
else:
    print("Game over!")
    print("The correct number was :", number)
    play_again = input("Do you want to play again ? (yes/ no) ")
    if play_again.lower() != "yes" :
        print("Thanks for playing!")
    breakpoint
      
     