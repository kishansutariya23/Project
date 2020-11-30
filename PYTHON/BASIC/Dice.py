#    SIMPLE DICE ROLLER (NUMBER GENERATION)
# just hit run button in your code editor to get random numbers of DICE



import random
def roll():
    return random.randint(1,6)
while True:
    print('when dice rolled we get')
    print(roll())
    break

