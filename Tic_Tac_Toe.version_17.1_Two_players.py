﻿print("Szanowni Gracze oto najwspanialsza na świecie wersja gry w kółko i krzyżyk.Plansza składa się z\
9 pól które są ponumerowe od 1 do 9\n Będziecie na zmianę proszeni o wybór pola. Pierwszy gracz\
będzie używać krzyżyków, drugi gracza będzie używać kółek.\
 Pola ponumerowane są według schematu poniżej")\

line_1=["1","2","3"]
line_2=["4","5","6"]
line_3=["7","8","9"]

def print_board():
    print(line_1)
    print(line_2)
    print(line_3)

print_board()
what_is_actually_in_field = []


def is_field_taken():
    if move in what_is_actually_in_field:
        return True
    else:
        return False

win_board = [] #po co jest ta lista
def win_check(current_player):

    if line_1 == (current_player,current_player,current_player):
        return True
    elif line_2 == (current_player,current_player,current_player):
        return True
    elif line_3 == (current_player,current_player,current_player):
         return True
    elif line_1[0] == current_player and line_2[0]==current_player and line_3[0]==current_player:
         return True
    elif line_1[1] == current_player and line_2[1]==current_player and line_3[1]==current_player:
         return True
    elif line_1[2] == current_player and line_2[2]==current_player and line_3[2]==current_player:
        return True
    elif line_1[0] == current_player and line_2[1]==current_player and line_3[2]==current_player:
        return True
    elif line_1[2] == current_player and line_2[1]==current_player and line_3[0]==current_player:
         return True


def make_move (player):
    global move
    move = input ("Drugi graczu wybierz prosze cyfre od 1 do 9 aby dodac '0'")

def check_which_field_is_taken (player):
    global line_1
    global line_2
    global line_3

    if move == "1":
        if is_field_taken() == False:
            line_1[0] = player
            what_is_actually_in_field.append(move)
        else:
            print("Pole jest już zajęte")
    elif move == "2":
        if is_field_taken() == False:
            line_1[1] = player
            what_is_actually_in_field.append(move)
        else:
            print("Pole jest już zajęte")
    elif move == "3":
        if is_field_taken() == False:
            line_1[2] = player
            what_is_actually_in_field.append(move)
        else:
            print("Pole jest już zajęte")
    elif move == "4":
        if is_field_taken() == False:
            line_2[0] = player
            what_is_actually_in_field.append(move)
        else:
            print("Pole jest już zajęte")
    elif move == "5":
        if is_field_taken() == False:
            line_2[1] = player
            what_is_actually_in_field.append(move)
        else:
            print("Pole jest już zajęte")
    elif move=="6":
        if is_field_taken() == False:
            line_2[2] = player
            what_is_actually_in_field.append(move)
        else:
            print("Pole jest już zajęte")
    elif move =="7":
        if is_field_taken()  == False:
            line_3[0] = player
            what_is_actually_in_field.append(move)
        else:
            print("Pole jest już zajęte")
    elif move == "8":
        if is_field_taken() == False:
            line_3[1] = player
            what_is_actually_in_field.append(move)
        else:
            print("Pole jest już zajęte")
    elif move == "9":
        if is_field_taken() == False:
            line_3[2] = player
            what_is_actually_in_field.append(move)
        else:
            print("Pole jest już zajęte")

    else:
        print("Graczu wybrałeś cyfrę z poza zakresu 1-9. Spróbuj jeszcze raz")


def automated_last_move (player,last_move):
    global line_1
    global line_2
    global line_3
    global what_is_actually_in_field

    k = 0
    while k < 100:

        if last_move == "1":
            if is_field_taken() == True:
                line_1[0] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif last_move == "2":
            if is_field_taken() == True:
                line_1[1] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif last_move == "3":
            if is_field_taken() == True:
                line_1[2] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif last_move  == "4":
            if is_field_taken() == True:
                line_2[0] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif last_move  == "5":
            if is_field_taken() == True:
                line_2[1] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif last_move == "6":
            if is_field_taken() == True:
                line_2[2] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif last_move == "7":
            if is_field_taken() == True:
                line_3[0] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif last_move == "8":
            if is_field_taken() == True:
                line_3[1] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif last_move == "9":
            if is_field_taken() == True:
                line_3[2] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
            what_is_actually_in_field.append(move)
    k+= 1
i = 0
while i<4:
    n = 0
    while n < 100:
        make_move("X")
        check_which_field_is_taken("X")
        print_board()
        n+= 1
    if win_check("X") == True:
        print("Graczu pierwszy wygrałeś. Gratulacje!!!")
        break

    make_move("O")
    check_which_field_is_taken("O")
    print_board()
    if win_check("O") == True:
        print("Graczu drugi wygrałeś. Gratulacje!!!")
        break
    i+= 1


if i == 4:
    for last_move in range(1,10):# Mam tu inty od 1 do 9
        last_move = str(last_move) # last_move staje się tu stringiem
        if last_move not in what_is_actually_in_field:
            automated_last_move("X", last_move) # W tej funkcji cyfry są stringami
    if win_check("X") is True:
        print("Graczu pierwszy wygrałeś. Gratulacje!!!")
    else:
        print("Żaden z graczy nie wygrał")

print_board()








