import os
import time
import sys

def groeting():
    os.system("cls")
    groeting.start = input(" |a|: nieuwe woordenlijst maken. \n "
                           "|b|: woorden toe te voegen aan een woordenlijst. \n "
                           "|h|: woordenlijst veranderen. \n |x|: woordelijst verwijderen. \n "
                           "|s|: Overhoren. \n "
                           "|q|: Stoppen met het programma. \n")

def nieuwe_lijst_naam():
    print("\n" * 30)
    naam_woordenlijst = input("Hoe wil je je woordenlijst noemen? ")
    bestaat_al = os.path.isfile(naam_woordenlijst)
    if bestaat_al:
        print("\n" * 5)
        print("bestand " + naam_woordenlijst + " bestaat al")
        print("\n" * 1)
    else:
        with open(naam_woordenlijst,"w+") as f:
            f.write("Bestand is aangemaakt")
        print("\n" * 5)
        print("Nieuwe woorden lijst - " + naam_woordenlijst + " - is gemaakt.")
        print("\n" * 2)
    main()

def lijst_verwijderen():
    print("\n" * 11)
    del_lijst = input("Welke lijst wil je verwijderen? ")
    bestaat_lijst_del = os.path.isfile(del_lijst)
    if bestaat_lijst_del:
        os.remove(del_lijst)
        print("\n" * 5)
        print("Lijst - " + del_lijst +  " - is succesvol verwijdert.")
        print("\n" * 1)
        main()
    else:
        print("\n" * 5)
        print("Bestand bestaat niet, dus kan het ook niet verwijdert worden!\n")
        main()


def overhoren():
    lijst_overhoor = input("Welke lijst wil je overhoren? ")
    bestaat_lijst_overhoor = os.path.isfile(lijst_overhoor)
    if bestaat_lijst_overhoor:
        print("Je kan worden overhoort.")
    else:
        print("\n" * 5)
        print("Bestand kan niet worden overhoort.")
        print("\n" * 1)
        main()

def geef_afscheid():
    print("Dit programma sluit over 5 seconden,")
    print("5")
    time.sleep(0.5)
    print("4")
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("0")
    time.sleep(0.5)
    sys.exit()

def voeg_woorden_toe():
    print("Voeg woorden toe")
    lijst_keuze = input("Naar welke lijst wil je toe?")
    bestaat_lijst = os.path.isfile(lijst_keuze)
    if bestaat_lijst == True:
        nederlands = ""
        ander_taal = input("naar welke taal wil je vertalen: ")
        while (nederlands != "q"):
            nederlands = input("Nederlands woord: ")
            ander_taal = input(ander_taal + " woord: ")

    else:
        print("Bestand bestaat niet")
        main()

def verander_woordenlijst():
    print("Verander woordenlijst")


def main():
    groeting()
    if groeting.start == "a":
        nieuwe_lijst_naam()
    if groeting.start == "b":
        voeg_woorden_toe()
    if groeting.start == "h":
        verander_woordenlijst()
    if groeting.start == "x":
        lijst_verwijderen()
    if groeting.start == "s":
        overhoren()
    if groeting.start == "q":
        geef_afscheid()


main()