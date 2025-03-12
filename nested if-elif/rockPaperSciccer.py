
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game=[rock,paper,scissors]
import random
cc =random.randint(0,2)
print(cc)
print(game[cc])
uc= int(input('Enter your choice \n 0 for rock\n 1 for paper\n 2 for scissor'))
print(f'The computer has choose {game[cc]}')
print(f' You choice is {game[uc]}')
if uc==2 and cc==0:
    print('computer win')
elif uc==0 and cc==2:
    print('you win')
elif uc>cc:
    print('you win')
elif cc>uc:
    print('comp win')