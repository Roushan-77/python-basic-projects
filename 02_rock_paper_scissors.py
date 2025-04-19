import random

# welcome to rock paper scissors game 
# 1 is for rock 
# 2 is for paper
# 3 is for scissors

# rules:
# rock can defeat scissors but can't paper
# paper can defeat rock but can't scissors
# scissors can defeat paper but can't rock

# keep in the mind:
# choose the given option 

def start():
    player = int(input("1. rock\n2. paper\n3. scissors\nyour choice: "))
    return player
while True:
    element = {
        1 : "rock",
        2 : "paper",
        3 : "scissors"
    }

    print("rock paper scissors game start")
    while True:
        player = start()
        if player in (1,2,3):
            break
        else:
            print("choose a valid option")

    bot = random.choice(list(element.keys()))


    player_choice = element[player]
    bot_choice = element[bot]

    print(f"you choosed : {player_choice}")
    print(f"bot choosed : {bot_choice}")

    if(player == bot):
        print("match tied")
    elif((player == 1 and bot == 2)or(player == 2 and bot == 3)or(player == 3 and bot == 1)):
        print("you lost and bot won")
    elif((player == 1 and bot == 3)or(player == 2 and bot == 1)or(player == 3 and bot == 2)):
        print("you won and bot lost")
    else:
        print("invalid input")

    again = input("wanna play again? (yes/no): ").strip().lower()
    if(again != 'yes'):
        print("i hope you enjoyed the game!\nThanks for playing")
        break