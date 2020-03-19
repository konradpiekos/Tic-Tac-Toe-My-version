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

def make_move (player_X,player_O):
    global line_1
    global line_2
    global line_3
    gracz_X = "Pierwszy graczu"
    gracz_O ="Drugi graczu"
    move=input("{} wybierz proszę cyfrę od 1 do 9 przypisaną do wolnego pola aby dodać X: ".format(gracz_X))

    if move=="1":
        line_1=[player_X,"2","3"]
    elif move=="2":
        line_1=["1",player_X,"3"]
    elif move=="3":
        line_1=["1","2",player_X]
    elif move=="4":
        line_2=[player_X,"5","6"]
    elif move=="5":
        line_2=["4",player_X,"6"]
    elif move=="6":
        line_2=["4","5",player_X]
    elif move=="7":
        line_3=[player_X,"8","9"]
    elif move=="8":
        line_3=["7",player_X,"9"]
    elif move=="9":
        line_3=["7","8",player_X]
    else:
      print("Graczu wybrałeś cyfrę poza zakresu 1-9. Spróbuj jeszcze raz")
    print_board()

    move=input("{} wybierz proszę cyfrę od 1 do 9 przypisaną do wolnego pola aby dodać O: ".format(gracz_O))
    if move=="1":
        line_1=[player_O,"2","3"]
    elif move=="2":
        line_1=["1",player_O,"3"]
    elif move=="3":
        line_1=["1","2",player_O]
    elif move=="4":
        line_2=[player_O,"5","6"]
    elif move=="5":
        line_2=["4",player_O,"6"]
    elif move=="6":
        line_2=["4","5",player_O]
    elif move=="7":
        line_3=[player_O,"8","9"]
    elif move=="8":
        line_3=["7",player_O,"9"]
    elif move=="9":
        line_3=["7","8",player_O]
    else:
      print("Graczu wybrałeś cyfrę poza zakresu 1-9. Spróbuj jeszcze raz")
    print_board()


make_move("X","O")
