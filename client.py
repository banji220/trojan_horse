import random 

def game():
    number = random.randint(0, 10)
    tries = 1
    done = False
    
    while not done:
        guess = int(input("Enter a guess: "))
        
        if guess == number:
            done = True
            print("You won!")
        else:
            tries += 1
            if guess > number: 
                print("The actual number was smaller!")
            else:
                print("The actual number was larger!")
    
    print(f"You needer {tries} tries!")

game = game()
game