import random

player = 0
computer = 0

def play():
    global computer
    global player
    print("Choisissez, 'Pierre'(1), 'feuille'(2), ou 'ciseaux'(3), le premier arrivé à 3 points gagne.")
    rep_uti = int(input())
    rep_comput = random.randint(1, 3)
    if rep_uti == 1 and rep_comput == 2:
        computer += 1
    if rep_uti == 1 and rep_comput == 3:
        player += 1
    if rep_uti == 2 and rep_comput == 1:
        player += 1
    if rep_uti == 2 and rep_comput == 3 :
        computer += 1
    if rep_uti == 3 and rep_comput == 1:
        computer += 1
    if rep_uti == 3 and rep_comput == 2:
        player += 1
    print(rep_comput)
    print (player,computer)


while True :
    play()
    if player == 3 or computer == 3 :
        break
if player > computer :
    print("Félicitations, vous avez gagné !")
if player < computer :
    print("Perdu! :(")