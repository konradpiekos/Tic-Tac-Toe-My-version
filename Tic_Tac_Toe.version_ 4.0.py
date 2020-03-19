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

def make_move (player_X,player_O,player_X_2):
    global line_1
    global line_2
    global line_3
    gracz_X = "Pierwszy graczu"
    gracz_O ="Drugi graczu"
    move_1=input("{} wybierz proszę cyfrę od 1 do 9 przypisaną do wolnego pola aby dodać X: ".format(gracz_X))

    if move_1=="1":
        line_1=[player_X,"2","3"]
    elif move_1=="2":
        line_1=["1",player_X,"3"]
    elif move_1=="3":
        line_1=["1","2",player_X]
    elif move_1=="4":
        line_2=[player_X,"5","6"]
    elif move_1=="5":
        line_2=["4",player_X,"6"]
    elif move_1=="6":
        line_2=["4","5",player_X]
    elif move_1=="7":
        line_3=[player_X,"8","9"]
    elif move_1=="8":
        line_3=["7",player_X,"9"]
    elif move_1=="9":
        line_3=["7","8",player_X]
    else:
      print("Graczu wybrałeś cyfrę poza zakresu 1-9. Spróbuj jeszcze raz")
    print_board()

    move_2=input("{} wybierz proszę cyfrę od 1 do 9 przypisaną do wolnego pola aby dodać O: ".format(gracz_O))
    if move_2 == move_1:
        print("Graczu wybrałeś zajęte pole, spróbuj jeszcze raz")
        move_2=input("{} wybierz proszę cyfrę od 1 do 9 przypisaną do wolnego pola aby dodać O: ".format(gracz_O))
    elif move_2=="1":
        line_1=[player_O,"2","3"]
    elif move_2=="2":
        line_1=["1",player_O,"3"]
    elif move_2=="3":
        line_1=["1","2",player_O]
    elif move_2=="4":
        line_2=[player_O,"5","6"]
    elif move_2=="5":
        line_2=["4",player_O,"6"]
    elif move_2=="6":
        line_2=["4","5",player_O]
    elif move_2=="7":
        line_3=[player_O,"8","9"]
    elif move_2=="8":
        line_3=["7",player_O,"9"]
    elif move_2=="9":
        line_3=["7","8",player_O]
    else:
      print("Graczu wybrałeś cyfrę poza zakresu 1-9. Spróbuj jeszcze raz")
    print_board()

    move_3=input("{} wybierz proszę cyfrę od 1 do 9 przypisaną do wolnego pola aby dodać X: ".format(gracz_X))
    if move_3 == move_1:
        print("Graczu wybrałeś zajęte pole, spróbuj jeszcze raz")
        move_3=input("{} wybierz proszę cyfrę od 1 do 9 przypisaną do wolnego pola aby dodać O: ".format(gracz_O))
    if move_3 == move_2:
        print("Graczu wybrałeś zajęte pole, spróbuj jeszcze raz")
        move_3=input("{} wybierz proszę cyfrę od 1 do 9 przypisaną do wolnego pola aby dodać O: ".format(gracz_O))
    if move_3=="1":
        line_1=[player_X_2,"2","3"]
    elif move_3=="2":
        line_1=["1",player_X_2,"3"]
    elif move_3=="3":
        line_1=["1","2",player_X_2]
    elif move_3=="4":
        line_2=[player_X_2,"5","6"]
    elif move_3=="5":
        line_2=["4",player_X_2,"6"]
    elif move_3=="6":
        line_2=["4","5",player_X_2]
    elif move_3=="7":
        line_3=[player_X_2,"8","9"]
    elif move_3=="8":
        line_3=["7",player_X_2,"9"]
    elif move_3=="9":
        line_3=["7","8",player_X_2]
    else:
      print("Graczu wybrałeś cyfrę poza zakresu 1-9. Spróbuj jeszcze raz")
    print_board()


make_move("X","O","X")


