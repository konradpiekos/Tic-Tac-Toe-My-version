print("Szanowni Gracze oto najwspanialsza na świecie wersja gry w kółko i krzyżyk.Plansza składa się z\
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
what_is_not_actually_in_field = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]



def is_field_taken():
    if move in what_is_actually_in_field: #Move nie jest argumentem funkcji make_move, tylko wartością zmienną w tej funkcji
        return True
    else:
        return False

def win_check(current_player):

    if line_1 == (current_player,current_player,current_player):
        return True
    elif line_2 == (current_player,current_player,current_player):
        return True
    elif line_3 == (current_player,current_player,current_player):
         return True
    elif line_1[0] == current_player and line_2[0] == current_player and line_3[0] == current_player:
         return True
    elif line_1[1] == current_player and line_2[1] == current_player and line_3[1] == current_player:
         return True
    elif line_1[2] == current_player and line_2[2] == current_player and line_3[2] == current_player:
        return True
    elif line_1[0] == current_player and line_2[1] == current_player and line_3[2] == current_player:
        return True
    elif line_1[2] == current_player and line_2[1] == current_player and line_3[0] == current_player:
         return True


def make_move (player):
    global what_is_actually_in_field
    global prompt_begin
    global sign
    global move

    if player == "X":
        prompt_begin = "Pierwszy"
        sign = "X"
    else:
        prompt_begin = "Drugi"
        sign = "O"
    move = input("{} graczu wybierz prosze cyfre od 1 do 9 aby dodac {}: ".format(prompt_begin,sign))

def check_which_field_is_taken (player):
    global line_1
    global line_2
    global line_3
    k = 0
    while k < 100:
        if move == "1":
            if is_field_taken() == False:
                line_1[0] = player
                what_is_actually_in_field.append(move)
                what_is_not_actually_in_field.remove(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move == "2":
            if is_field_taken() == False:
                line_1[1] = player
                what_is_actually_in_field.append(move)
                what_is_not_actually_in_field.remove(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move == "3":
            if is_field_taken() == False:
                line_1[2] = player
                what_is_actually_in_field.append(move)
                what_is_not_actually_in_field.remove(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move == "4":
            if is_field_taken() == False:
                line_2[0] = player
                what_is_actually_in_field.append(move)
                what_is_not_actually_in_field.remove(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move == "5":
            if is_field_taken() == False:
                line_2[1] = player
                what_is_actually_in_field.append(move)
                what_is_not_actually_in_field.remove(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move=="6":
            if is_field_taken() == False:
                line_2[2] = player
                what_is_actually_in_field.append(move)
                what_is_not_actually_in_field.remove(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move =="7":
            if is_field_taken()  == False:
                line_3[0] = player
                what_is_actually_in_field.append(move)
                what_is_not_actually_in_field.remove(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move == "8":
            if is_field_taken() == False:
                line_3[1] = player
                what_is_actually_in_field.append(move)
                what_is_not_actually_in_field.remove(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move == "9":
            if is_field_taken() == False:
                line_3[2] = player
                what_is_actually_in_field.append(move)
                what_is_not_actually_in_field.remove(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        else:
            print("Graczu wybrałeś cyfrę z poza zakresu 1-9. Spróbuj jeszcze raz")

        k+= 1

ooo_move_digit = 0

def ooo_xxx_move (current_player):
    global ooo_move_digit
    if line_1[0] == current_player and line_1[1] == current_player and "3" not in what_is_actually_in_field:
        ooo_move_digit = "3"
        # Gdy zamiast funkcji próbuję tylko podać wartość computer_move pojawia się błąd
    elif line_1[0] == current_player and line_1[2] == current_player and "2" not in what_is_actually_in_field:
        ooo_move_digit = "2"
    elif line_1[1] == current_player and line_1[2] == current_player and "1" not in what_is_actually_in_field:
        ooo_move_digit = "1"
    elif line_2[0] == current_player and line_2[1] == current_player and "6" not in what_is_actually_in_field:
        ooo_move_digit = "6"
    elif line_2[0] == current_player and line_2[2] == current_player and "5" not in what_is_actually_in_field:
        ooo_move_digit = "5"
    elif line_2[1] == current_player and line_2[2] == current_player and "4" not in what_is_actually_in_field:
        ooo_move_digit = "4"
    elif line_3[0] == current_player and line_3[1] == current_player and "9" not in what_is_actually_in_field:
        ooo_move_digit = "9"
    elif line_2[2] == current_player and line_3[2] == current_player and "3" not in what_is_actually_in_field:
        ooo_move_digit  = "3"
    elif line_1[2] == current_player and line_2[1] == current_player and "3" not in what_is_actually_in_field:
        ooo_move_digit = "3"
    elif line_3[0] == current_player and line_3[2] == current_player and "8" not in what_is_actually_in_field:
        ooo_move_digit = "8"
    elif line_3[1] == current_player and line_3[2] == current_player and "7" not in what_is_actually_in_field:
        ooo_move_digit = "7"
    elif line_1[0] == current_player and line_2[0] == current_player and "7" not in what_is_actually_in_field:
        ooo_move_digit = "7"
    elif line_1[0] == current_player and line_3[0] == current_player and "4" not in what_is_actually_in_field:
        ooo_move_digit = "4"
    elif line_2[0] == current_player and line_3[0] == current_player and "1" not in what_is_actually_in_field:
        ooo_move_digit = "1"
    elif line_1[1] == current_player and line_2[1] == current_player and "8" not in what_is_actually_in_field:
        ooo_move_digit = "8"
    elif line_1[1] == current_player and line_3[1] == current_player and "5" not in what_is_actually_in_field:
        ooo_move_digit = "5"
    elif line_2[1] == current_player and line_3[1] == current_player and "2" not in what_is_actually_in_field:
        ooo_move_digit = "2"
    elif line_1[2] == current_player and line_2[2] == current_player and "9" not in what_is_actually_in_field:
        ooo_move_digit = "9"
    elif line_1[2] == current_player and line_3[2] == current_player and "6" not in what_is_actually_in_field:
        ooo_move_digit = "6"
    elif line_1[0] == current_player and line_2[1] == current_player and "9" not in what_is_actually_in_field:
        ooo_move_digit = "9"
    elif line_1[0] == current_player and line_3[2] == current_player and "5" not in what_is_actually_in_field:
        ooo_move_digit = "5"
    elif line_2[1] == current_player and line_3[2] == current_player and "1" not in what_is_actually_in_field:
        ooo_move_digit = "1"
    elif line_1[2] == current_player and line_2[1] == current_player and "7" not in what_is_actually_in_field:
        ooo_move_digit = "7"
    elif line_1[2] == current_player and line_3[0] == current_player and "5" not in what_is_actually_in_field:
        ooo_move_digit = "5"
    else:
        None


def random_move ():
    import random
    random_move = random.choice(what_is_not_actually_in_field)
    random_move = str(random_move)
    applying_automated_move ("O",random_move)


def automated_move ():
    ooo_xxx_move("O")
    if ooo_move_digit != 0:
        applying_automated_move("O", ooo_move_digit) #Błąd
        return
    ooo_xxx_move("X")
    if ooo_move_digit != 0:
        applying_automated_move("O", ooo_move_digit)
        return
    random_move()


def applying_automated_move (current_player,computer_move):
    global line_1
    global line_2
    global line_3
    global what_is_actually_in_field

    if computer_move == "1":
        line_1[0] = current_player
    elif computer_move == "2":
        line_1[1] = current_player
    elif computer_move == "3":
        line_1[2] = current_player
    elif computer_move  == "4":
        line_2[0] = current_player
    elif computer_move  == "5":
        line_2[1] = current_player
    elif computer_move == "6":
        line_2[2] = current_player
    elif computer_move == "7":
        line_3[0] = current_player
    elif computer_move == "8":
        line_3[1] = current_player
    elif computer_move == "9":
        line_3[2] = current_player
    print ("Comp move:", computer_move)
    what_is_actually_in_field.append(computer_move)
    what_is_not_actually_in_field.remove(computer_move)



def automated_last_move (player,last_move):
    global line_1
    global line_2
    global line_3
    global what_is_actually_in_field

    k = 0
    while k < 100:

        if last_move == "1":
            line_1[0] = player
            what_is_actually_in_field.append(last_move)
            break
        elif last_move == "2":
            line_1[1] = player
            what_is_actually_in_field.append(last_move)
            break
        elif last_move == "3":
            line_1[2] = player
            what_is_actually_in_field.append(last_move)
            break
        elif last_move  == "4":
            line_2[0] = player
            what_is_actually_in_field.append(last_move)
            break
        elif last_move  == "5":
            line_2[1] = player
            what_is_actually_in_field.append(last_move)
            break
        elif last_move == "6":
            line_2[2] = player
            what_is_actually_in_field.append(last_move)
            print ("znacznik 1")
            break
        elif last_move == "7":
            line_3[0] = player
            what_is_actually_in_field.append(last_move)
            break
        elif last_move == "8":
            line_3[1] = player
            what_is_actually_in_field.append(last_move)
            break
        elif last_move == "9":
            line_3[2] = player
            what_is_actually_in_field.append(last_move)
            break


    k+= 1
i = 0
while i < 4:

    # print (what_is_actually_in_field)
    # print(what_is_not_actually_in_field)
    make_move("X")
    check_which_field_is_taken("X")
    print_board()
    if win_check("X") == True:
        print("Graczu pierwszy wygrałeś. Gratulacje!!!")
        break

    print (what_is_actually_in_field)
    print(what_is_not_actually_in_field)
    automated_move()
    print ("Pole do ataku lub obrony: ", ooo_move_digit)
    print ("Wolne pola: ",what_is_not_actually_in_field)# Ruch automatyczny musi zostać wykonany przed ruchem manualnym
    print_board()
    if win_check("O") is True:
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








