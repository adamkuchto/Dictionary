"""
Słownik, zadanie z kursu "python 3 od podstaw do eksperta - udemy
1. Dodanie czytania słownika z pliku
2. GUI
"""


slownik = {'kot':'zwierzak', 'auto':'pojazd', 'pomidor': 'warzywo'
}
        
print("*** Słownik definicji ***\n")

while(True):
    print("     MENU        \n1: Dodaj definicję:\n2: Szukaj definicji:\n3: Usuń defifnicję:\n 'Q' - Wyjście\n")
    choose = input()
    if(choose == "1"):
        print("Dodaj definicję: ")
        haslo = input("Podaj hasło: ")
        definicja = input("Podaj definicje: ")  
        slownik[haslo] = definicja


    elif(choose == "2"):
        print("Szukaj definicji: ")
        szukaj = input("Wprowadź haslo: ")
        if szukaj in slownik:
            print(slownik[szukaj])
            print("\n")
        else:
            print("Słownik nie zawiera hasła którego szukasz")



    elif(choose == "3"):
        usun = input("Usuń defifnicję: ")
        if usun in slownik:
            del(slownik[usun])
        else:
            print("Brak hasła")



    elif(choose == "q" or choose == "Q"):
        break


    else:
        print("Nie ma takiej opcji w menu")


