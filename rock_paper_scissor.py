import random

item = ['rock', 'paper', 'scissor']
itemRelation = {'rock': 'scissor',
                'paper': 'rock',
                'scissor': 'paper'}
p1 = ""
p2 = ""
score1 = 0
score2 = 0


def init():
    global p1
    p1 = input("Choose between rock, paper or scissor  ")
    global p2
    p2 = random.choice(item)

    while p1 not in item:
        print("This word is not available")
        init()


def play():
    global score1
    global score2
    global p1
    global p2

    if p1 == p2:
        print(p1 + " vs " + p2 + ' : draw !')
    elif p2 == itemRelation[p1]:
        score1 += 1
        print(p1 + " vs " + p2 + " : you win !")
    else:
        score2 += 1
        print(p1 + " vs " + p2 + " : you loose !")


def score():
    print('you ' + str(score1) + ' / bot ' + str(score2))


def end():
    if score1 > score2:
        print('Game finished ! You win :)')
    else:
        print('Game finished ! You loose :(')


def start():
    while score1 < 3 and score2 < 3:
        init()
        play()
        score()
    end()


start()
