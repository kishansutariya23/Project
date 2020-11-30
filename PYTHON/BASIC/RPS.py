# this is simple ROCK, PAPER, SCISSOR game 
# you can find same concept with custamized way while playing this game in my reposotory==>Project/PYTHON/BASIC/Rock-Paper-Scissor.py 
import random
player1p=player2p=0
l=['rock','paper','scissor']
player1=random.choice(l)
player2=random.choice(l)
print(player1,player2)
if player1=='rock' and player2=='paper':
    player2p +=1
elif player1=='scissor' and player2=='paper':
    player1p +=1
elif player1=='paper' and player2=='rock':
    player1p +=1
elif player1=='paper' and player2=='scissor':
    player2p +=1
elif player1=='scissor' and player2=='rock':
    player2p +=1
elif player1=='rock' and player2=='scissor':
    player1p+=1
else:
    print('Both are SAME')


print('Player 1 points are:',player1p)
print('Player 2 points are:',player2p)
