import os
import time
import sys

def groeting():
    os.system("cls")
    groeting.start = input("|a|: Nieuwe woordenlijst maken. \n |b|: woorden toe te voegen aan een woordenlijst. \n |h|: woordenlijst veranderen. \n |x|: woordelijst verwijderen. \n |s| Overhoren. \n |q|: Stoppen met het programma. \n")

def nieuwe_lijst_naam():
    naam_woordenlijst = input("Hoe wil je je woordenlijst noemen? ")
    with open(naam_woordenlijst,"w+") as f:
      f.write("Bestand is aangemaakt")

def lijst_verwijderen():
    del_lijst = input("Welke lijst wil je verwijderen? ")
    bestaat_lijst_del = os.path.isfile(del_lijst)
    if bestaat_lijst_del:
        os.remove(del_lijst)
        print("Lijst " + del_lijst + " is succesvol verwijdert.")
    else:
        print("Bestand bestaat niet, dus kan het ook niet verwijdert worden!")


def overhoren():
    print(" Overhoren")

def geef_afscheid():
    print("Dit programma sluit over 5 seconden")
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
    sys.exit()

def voeg_woorden_toe():
    print("Voeg woorden toe")
    lijst_keuze = input("Naar welke lijst wil je toe.")
    bestaat_lijst = os.path.isfile(lijst_keuze)
    if bestaat_lijst == True:
        print("bestaat")
    else:
        print("Bestand bestaat niet")

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