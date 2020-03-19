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

win_board=[] #po co jest ta lista
def win_check(current_player):

    if line_1 ==(current_player,current_player,current_player):
        return True
    elif line_2 ==(current_player,current_player,current_player):
        return True
    elif line_3 ==(current_player,current_player,current_player):
         return True
    elif line_1[0]== current_player and line_2[0]==current_player and line_3[0]==current_player:
         return True
    elif line_1[1]== current_player and line_2[1]==current_player and line_3[1]==current_player:
         return True
    elif line_1[2]== current_player and line_2[2]==current_player and line_3[2]==current_player:
        return True
    elif line_1[0]== current_player and line_2[1]==current_player and line_3[2]==current_player:
        return True
    elif line_1[2]== current_player and line_2[1]==current_player and line_3[0]==current_player:
         return True


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
    j=0 #czemu ta pętla jest w tym miejscu? bo program ma zapytać jedego gracza gdy jest jego kolejność jaką cyfrę wybiera aż 100razy
    while j<100:
        j+=1 #gdy tu będzie 2, pętla zostanie wykonana 50razy?

        move=input("{} graczu wybierz proszę cyfrę od 1 do 9 aby dodać {}: ".format(prompt_begin,sign))

        if move=="1":
            if is_field_taken()==False:
                line_1[0]=player
                what_is_actually_in_field.append(move)#dodajemy wartość move do listy what_is_actually_in_field
                break #przy funkcji if nie było wcześniej break
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
    print_board()
    if win_check("X")==True:
        print("Graczu pierwszy wygrałeś. Gratulacje!!!")
        break


    make_move("O")
    print_board()
    if win_check("O")==True:
        print("Graczu drugi wygrałeś. Gratulacje!!!")
        break
if i==4:
    make_move("X")#to powinno się odpalić gdy pętla została wykonana 4 razy
    print_board()
    if win_check("X")==True:
        print("Graczu pierwszy wygrałeś. Gratulacje!!!")
    else:
        print("Żaden z graczy nie wygrał")#w ostatnim rozdaniu może wygrać gracz X,





