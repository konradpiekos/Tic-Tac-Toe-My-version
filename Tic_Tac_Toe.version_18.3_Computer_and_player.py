print("Szanowni Gracze oto najwspanialsza na świecie wersja gry w kółko i krzyżyk.Plansza składa się z")
print("9 pól które są ponumerowe od 1 do 9. Będziecie na zmianę proszeni o wybór pola. Pierwszy gracz")
print("będzie używać krzyżyków, drugi gracza będzie używać kółek.")
print("Pola ponumerowane są według schematu poniżej")

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
    if move in what_is_actually_in_field: #Move nie jest argumentem funkcji make_move, tylko wartością zmienną w tej funkcji
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
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move == "2":
            if is_field_taken() == False:
                line_1[1] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move == "3":
            if is_field_taken() == False:
                line_1[2] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move == "4":
            if is_field_taken() == False:
                line_2[0] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move == "5":
            if is_field_taken() == False:
                line_2[1] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move=="6":
            if is_field_taken() == False:
                line_2[2] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move =="7":
            if is_field_taken()  == False:
                line_3[0] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move == "8":
            if is_field_taken() == False:
                line_3[1] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        elif move == "9":
            if is_field_taken() == False:
                line_3[2] = player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
                make_move(player)
        else:
            print("Graczu wybrałeś cyfrę z poza zakresu 1-9. Spróbuj jeszcze raz")

        k+= 1

def automated_move (current_player):
    if line_1[0] == current_player and line_1[1] == current_player and "3" not in what_is_actually_in_field:
        applying_automated_move (current_player,"3")# Gdy zamiast funkcji próbuję tylko podać wartość computer_move pojawia się błąd
    elif line_1[0] == current_player and line_1[2] == current_player and "2" not in what_is_actually_in_field:
        applying_automated_move(current_player, "2")
    elif line_1[1] == current_player and line_1[2] == current_player and "1" not in what_is_actually_in_field:
        applying_automated_move(current_player,"1")





def applying_automated_move (player,computer_move):
    global line_1
    global line_2
    global line_3
    global what_is_actually_in_field

    a = 0
    while a < 100:

        if computer_move == "1":
            if is_field_taken() == True: # Ten wiersz jest zbędny. Został usunięty w wersji 18.4
                line_1[0] = player
                what_is_actually_in_field.append(computer_move)
                break
            else:
                print("Pole jest już zajęte")
        elif computer_move == "2":
            if is_field_taken() == True:
                line_1[1] = player
                what_is_actually_in_field.append(computer_move)
                break
            else:
                print("Pole jest już zajęte")
        elif computer_move == "3":
            if is_field_taken() == True:
                line_1[2] = player
                what_is_actually_in_field.append(computer_move)
                break
            else:
                print("Pole jest już zajęte")
        elif computer_move  == "4":
            if is_field_taken() == True:
                line_2[0] = player
                what_is_actually_in_field.append(computer_move)
                break
            else:
                print("Pole jest już zajęte")
        elif computer_move  == "5":
            if is_field_taken() == True:
                line_2[1] = player
                what_is_actually_in_field.append(computer_move)
                break
            else:
                print("Pole jest już zajęte")
        elif computer_move == "6":
            if is_field_taken() == True:
                line_2[2] = player
                what_is_actually_in_field.append(computer_move)
                break
            else:
                print("Pole jest już zajęte")
        elif computer_move == "7":
            if is_field_taken() == True:
                line_3[0] = player
                what_is_actually_in_field.append(computer_move)
                break
            else:
                print("Pole jest już zajęte")
        elif computer_move == "8":
            if is_field_taken() == True:
                line_3[1] = player
                what_is_actually_in_field.append(computer_move)
                break
            else:
                print("Pole jest już zajęte")
        elif computer_move == "9":
            if is_field_taken() == True:
                line_3[2] = player
                what_is_actually_in_field.append(computer_move)
                break
            else:
                print("Pole jest już zajęte")
        a+= 1

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

    make_move("X")
    check_which_field_is_taken("X")
    print_board()
    if win_check("X") == True:
        print("Graczu pierwszy wygrałeś. Gratulacje!!!")
        break

    automated_move("O") # Ruch automatyczny musi zostać wykonany przed ruchem manualnym
    print_board()
    if win_check("O") == True:
        print("Graczu drugi wygrałeś. Gratulacje!!!")
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








