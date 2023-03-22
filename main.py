import random
choices=["rock","paper","scissors"]
comp_score=0
user_score=0

def play_game(comp_score,user_score):
    answer = random.randint(1, 3)

    your_input=int(input("what is your entry? 1. Rock, 2. Paper, 3. Scissors"))
    print("computer picked",choices[answer-1]+". which is  choice ",answer)
    did_you_win:bool =False
    if(your_input == 1 and answer==2):
        did_you_win=False

    elif (your_input ==1 and answer==3):
        did_you_win=True

    elif (your_input == 2 and answer == 1):
        did_you_win = True

    elif (your_input == 2 and answer == 3):
        did_you_win = False

    elif (your_input == 3 and answer == 1):
        did_you_win = False

    elif (your_input == 3 and answer == 2):
        did_you_win = True



    if (your_input == answer):
        print("you chose ", choices[answer-1] + " hence you drew")

    elif did_you_win:
            user_score =user_score+ 1
            print("you chose ", choices[answer-1] + " hence you won")
    else:
            comp_score=comp_score+1
            print("you chose ",choices[answer-1]+" hence you lost")

    print("comp score",comp_score)
    print("user score",user_score)


times_to_play:int =int(input("How many times do you want to play? "))

for play_situation in range(times_to_play):
    play_game(comp_score,user_score)






