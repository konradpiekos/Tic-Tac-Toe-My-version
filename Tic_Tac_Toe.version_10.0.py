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

what_is_actually_in_field=[]

def is_field_taken():
    if move in what_is_actually_in_field:
        return True
    else:
        return False

win_board=[]

    if line_1=("X","X","X"):
        print("Graczu pierwszy wygrałeś")
    elif line_1=("Y","Y","Y"):
        print("Graczu drugi wygrałeś")
    elif if line_2 =("X","X", "X"):
        print("Graczu pierwszy wygrałeś")
    elif line_2=("Y","Y","Y"):
        print("Graczu drugi wygrałeś")
    elif line_3=("X","X", "X"):
        print("Graczu pierwszy wygrałeś")
    elif line_3=("Y","Y","Y"):
        print("Graczu drugi wygrałeś")
    elif:
        line_1[0]="X"
        line_2[0]="X"
        line_3[0]="X"
        print("Graczu pierwszy wygrałeś")
     elif:
        line_1[0]="Y"
        line_2[0]="Y"
        line_3[0]="Y"
        print("Graczu drugi wygrałeś")

    elif line_1=("Y","Y","Y"):
        print("Graczu drugi wygrałeś")


def win_check(current_player):
    if current_player is in win_board:

def make_move (player):
    global line_1
    global line_2
    global line_3
    global what_is_actually_in_field
    global prompt_begin
    global sign
    global move

    if player =="X":
        prompt_begin = "Pierwszy"
        sign = "X"
    else:
        prompt_begin = "Drugi"
        sign = "O"
    j=0
    while j<100:
        j+=1

        move=input("{} graczu wybierz proszę cyfrę od 1 do 9 aby dodać {}: ".format(prompt_begin,sign))

        if move=="1":
            if is_field_taken()==False:
                line_1[0]=player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif move=="2":
            if is_field_taken()==False:
                line_1[1]=player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif move=="3":
            if is_field_taken()==False:
                line_1[2]=player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif move =="4":
            if is_field_taken()==False:
                line_2[0]=player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif move =="5":
            if is_field_taken()==False:
                line_2[1]=player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif move=="6":
            if is_field_taken()==False:
                line_2[2]=player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif move=="7":
            if is_field_taken()==False:
                line_3[0]=player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif move=="8":
            if is_field_taken()==False:
                line_3[1]=player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
        elif move=="9":
            if is_field_taken()==False:
                line_3[2]=player
                what_is_actually_in_field.append(move)
                break
            else:
                print("Pole jest już zajęte")
            what_is_actually_in_field.append(move)
        else:
            print("Graczu wybrałeś cyfrę poza zakresu 1-9. Spróbuj jeszcze raz")

i=0
while i<4:
    i+=1

    make_move("X")
    print(what_is_actually_in_field)
    print_board()
    make_move("O")
    print(what_is_actually_in_field)
    print_board()





