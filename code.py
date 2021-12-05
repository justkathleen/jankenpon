print("rock paper scissor game")
print("1 = rock")
print("2 = paper")
print("3 = scissor")
player = input("pick a number: ")
if player == "1":
    print("You choose rock")
elif player == "2":
    print("You choose paper")
elif player == "3":
    print("You choose scissor")
import random
luck = random.randint(1,3)
#print(luck)
if luck == 1:
    print ("computer chooses rock")
elif luck == 2:
    print("computer chooses paper")
elif luck == 3:
    print("computer chooses scissor")

if player == "1" and luck == 1:
    print("It's a tie")
elif player == "1" and luck ==2:
    print("paper beats rock")
    print("you lose")
elif player == "1" and luck ==3:
    print("rock beats scissor")
    print("you win")
elif player == "2" and luck ==1:
    print("paper beats rock")
    print("you win")
elif player == "2" and luck ==2:
    print("It's a tie")
elif player == "2" and luck ==3:
    print("scissor beats paper")
    print("you lose")
elif player == "3" and luck ==1:
    print("rock beats scissor")
    print("you lose")
elif player == "3" and luck ==2:
    print("scissor beats paper")
    print("you win")
elif player == "3" and luck ==3:
    print("It's a tie")
