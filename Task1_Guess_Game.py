import random
print("!! Welcome To Guess The Number Game !!")
num = random.randint(1,100)
guess = None

for i in range (1, num+1):
    guess = int(input("Enter your guess: "))
    if guess > num:
        print("Yoour guess is high")
    elif guess < num:
        print("Your guess is low")
    elif guess == num:
        print("You guessed it correctly!!")
        break

# while (guess!=num):
#      guess = int(input("Enter your guess: "))
#      if guess > num:
#         print("Yoour guess is high")
#      elif guess < num:
#         print("Your guess is low")
#      elif guess == num:
#         print("You guessed it correctly!!")
#         break
