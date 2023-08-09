## 'Snake Water and Gun Game' in this game gun can suit the snake and snake can drink the water and water can destroy the gun
def result(a,b):
    if(a==b):
      print("Its Draw")
    elif(a=='snake' and b=='water'):
       print("Sorry! You lose😢😢")
    elif(a=='snake' and b=='gun'):
       print("Wonderful! You won😍😍✌")
    elif(a=='water'and b=='gun'):
       print("Sorry! You lose😢😢")
    elif(a=='water' and b=='snake'):
       print("Wonderful! You won😍😍✌")
    elif(a=='gun' and b=='snake'):
       print("Sorry! You lose😢😢")
    elif(a=='gun' and b=='water'):
       print("Wonderful! You won😍😍✌")
    else:
       print("Please! Choose right option")
import random
resume=True
while(resume==True):
    list=['snake','water','gun']
    computer_choice=random.choice(list)
    # print(computer_choice)
##Choose by player
    player_choice=input("Please choose ['Snake','Water','Gun']\n").lower()
    print(f"You choose {player_choice} and other player choose {computer_choice}")
    result(computer_choice,player_choice)
    ask=input("Do you want to play again press['Y','N']\n").lower()
    if (ask=='y'):
       resume=True
    else:
       resume=False
       print("Thankuu Player")