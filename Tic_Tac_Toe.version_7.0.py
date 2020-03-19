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

def make_move (player):
    global line_1
    global line_2
    global line_3
    global what_is_actually_in_field
    if player =="X":
        prompt_begin = "Pierwszy"
        sign = "X"
    else:
        prompt_begin = "Drugi"
        sign = "O"
    move=input("{} graczu wybierz proszę cyfrę od 1 do 9 aby dodać {}: ".format(prompt_begin,sign))

    if move in what_is_actually_in_field:
        print("Graczu wybrałeś zajęte pole, spróbuj ponownie. ")
        move=input("{} graczu wybierz proszę cyfrę od 1 do 9 aby dodać {}: ".format(prompt_begin,sign))
    else:
        print()

    if move=="1":
        line_1[0]=player
        what_is_actually_in_field.append(move)
    elif move=="2":
        line_1[1]=player
        what_is_actually_in_field.append(move)
    elif move=="3":
        line_1[2]=player
        what_is_actually_in_field.append(move)
    elif move =="4":
        line_2[0]=player
        what_is_actually_in_field.append(move)
    elif move =="5":
        line_2[1]=player
        what_is_actually_in_field.append(move)
    elif move=="6":
        line_2[2]=player
        what_is_actually_in_field.append(move)
    elif move=="7":
        line_3[0]=player
        what_is_actually_in_field.append(move)
    elif move=="8":
        line_3[1]=player
        what_is_actually_in_field.append(move)
    elif move=="9":
        line_3[2]=player
        what_is_actually_in_field.append(move)
    else:
        print("Graczu wybrałeś cyfrę poza zakresu 1-9. Spróbuj jeszcze raz")



make_move("X")
print_board()

make_move("O")
print_board()

make_move("X")
print_board()
make_move("O")
print_board()
make_move("X")
print_board()
make_move("O")
print_board()
make_move("X")
print_board()
make_move("O") #dodać zaznaczanie ostatniego pola
print_board()

