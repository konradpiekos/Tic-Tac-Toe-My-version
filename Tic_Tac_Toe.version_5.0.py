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

def make_move (player):
    global line_1
    global line_2
    global line_3

    if player =="X" :
        move=input("Pierwszy graczu wybierz proszę cyfrę od 1 do 9 aby dodać X: ")
    else:
        move=input("Drugi graczu wybierz proszę cyfrę od 1 do 9 aby dodać O: ")
    if move=="1":
        line_1=[player,"2","3"]
    elif move=="2":
        line_1=["1",player,"3"]
    elif move=="3":
        line_1=["1","2",player]
    elif move=="4":
        line_2=[player,"5","6"]
    elif move=="5":
        line_2=["4",player,"6"]
    elif move=="6":
        line_2=["4","5",player]
    elif move=="7":
        line_3=[player,"8","9"]
    elif move=="8":
        line_3=["7",player,"9"]
    elif move=="9":
        line_3=["7","8",player]
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

