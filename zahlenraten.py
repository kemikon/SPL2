# zahlenRaten.py
import random
print("Willkommen:Das Spiel heißt - ZahlenRaten(Computer spielt mit sich selbst")
maxrange = input("Bitte MaxRange eingeben: ")
gewonnen = False
versuche = 1
zufallszahl = random.randint(1,maxrange)
print("Zufallszahl:", zufallszahl)
while(gewonnen == False):
    errattungDerZahl = maxrange/2
    if(erratungDerZahl == zufallszahl):
        gewonnen == True
        print("Computer hat gewonnen.", "Versuche: ", versuche )
            if(erratungDerZahl != zufallszahl):
                print("Zahl von dem Computer: ", errattungDerZahl)
                nichtErraten = input("Wenn die Zufallszahl ist > als die Zahl von dem computer, schreiben Sie 'nein', wenn die Zufallszahl ist < als die Zahl von dem Computer, schreiben Sie 'ja'")
                versuche = int(versuche+1)
                if(nichtErraten == "nein"):
                    errattungDerZahl = int(errattungDerZahl+(errattungDerZahl/2))
                    if(errattungDerZahl == zufallszahl):
                        gewonnen == True
                        print("Computer hat gewonnen.", "Versuche: ", versuche )
                    if(errattungDerZahl != zufallszahl):
                        print("Zahl von dem Computer: ", errattungDerZahl)
                        nichtErraten = input("Wenn die Zufallszahl ist > als die Zahl von dem computer, schreiben Sie 'nein', wenn die Zufallszahl ist < als die Zahl von dem Computer, schreiben Sie 'ja'")
                        versuche = int(versuche+1)
    if(nichtErraten == "ja"):
        errattungDerZahl = int(errattungDerZahl-(errattungDerZahl/2))
            if(errattungDerZahl == zufallszahl):
                gewonnen == True
                print("Computer hat gewonnen.", "Versuche: ", versuche )
                if(errattungDerZahl != zufallszahl):
                    print("Zahl von dem Computer: ", errattungDerZahl)
                    nichtErraten = input("Wenn die Zufallszahl ist > als die Zahl von dem computer, schreiben Sie 'nein', wenn die Zufallszahl ist < als die Zahl von dem Computer, schreiben Sie 'ja'")
                    versuche = int(versuche+1)
                    if(nichtErraten == "nein"):
                        errattungDerZahl = int(errattungDerZahl+(errattungDerZahl/4))
                        if(errattungDerZahl == zufallszahl):
                            gewonnen == True
                            print("Computer hat gewonnen.", "Versuche: ", versuche )
                        if(errattungDerZahl != zufallszahl):
                            print("Zahl von dem Computer: ", errattungDerZahl)
                            nichtErraten = input("Wenn die Zufallszahl ist > als die Zahl von dem computer, schreiben Sie 'nein', wenn die Zufallszahl ist < als die Zahl von dem Computer, schreiben Sie 'ja'")
                            versuche = int(versuche+1)
                    if(nichtErraten == "ja"):
                        errattungDerZahl = int(errattungDerZahl-(errattungDerZahl/2))
                        if(errattungDerZahl == zufallszahl):
                            gewonnen == True
                            print("Computer hat gewonnen.", "Versuche: ", versuche )
                        if(errattungDerZahl != zufallszahl):
                            print("Zahl von dem Computer: ", errattungDerZahl)
                            nichtErraten = input("Wenn die Zufallszahl ist > als die Zahl von dem computer, schreiben Sie 'nein', wenn die Zufallszahl ist < als die Zahl von dem Computer, schreiben Sie 'ja'")
                            versuche = int(versuche+1)
    if(nichtErraten == "ja"):
        errattungDerZahl = int(errattungDerZahl-(errattungDerZahl/2))
        if(errattungDerZahl == zufallszahl):
            gewonnen == True
            print("Computer hat gewonnen.", "Versuche: ", versuche )
        if(errattungDerZahl != zufallszahl):
            print("Zahl von dem Computer: ", errattungDerZahl)
            nichtErraten = input("Wenn die Zufallszahl ist > als die Zahl von dem computer, schreiben Sie 'nein', wenn die Zufallszahl ist < als die Zahl von dem Computer, schreiben Sie 'ja'")
            versuche = int(versuche+1)
            if(nichtErraten == "nein"):
                errattungDerZahl = int(errattungDerZahl+(errattungDerZahl/2))
                if(errattungDerZahl == zufallszahl):
                    gewonnen == True
                    print("Computer hat gewonnen.", "Versuche: ", versuche )
                if(errattungDerZahl != zufallszahl):
                    print("Zahl von dem Computer: ", errattungDerZahl)
                    nichtErraten = input("Wenn die Zufallszahl ist > als die Zahl von dem computer, schreiben Sie 'nein', wenn die Zufallszahl ist < als die Zahl von dem Computer, schreiben Sie 'ja'")
                    versuche = int(versuche+1)
            if(nichtErraten == "ja"):
                errattungDerZahl = int(errattungDerZahl-(errattungDerZahl/2))
                if(errattungDerZahl == zufallszahl):
                    gewonnen == True
                    print("Computer hat gewonnen.", "Versuche: ", versuche )
                if(errattungDerZahl != zufallszahl):
                    print("Zahl von dem Computer: ", errattungDerZahl)
                    nichtErraten = input("Wenn die Zufallszahl ist > als die Zahl von dem computer, schreiben Sie 'nein', wenn die Zufallszahl ist < als die Zahl von dem Computer, schreiben Sie 'ja'")
                    versuche = int(versuche+1)
                    if(nichtErraten == "nein"):
                        errattungDerZahl = int(errattungDerZahl+(errattungDerZahl/4))
                        if(errattungDerZahl == zufallszahl):
                            gewonnen == True
                            print("Computer hat gewonnen.", "Versuche: ", versuche )
                        if(errattungDerZahl != zufallszahl):
                            print("Zahl von dem Computer: ", errattungDerZahl)
                            nichtErraten = input("Wenn die Zufallszahl ist > als die Zahl von dem computer, schreiben Sie 'nein', wenn die Zufallszahl ist < als die Zahl von dem Computer, schreiben Sie 'ja'")
                            versuche = int(versuche+1)
                    if(nichtErraten == "ja"):
                        errattungDerZahl = int(errattungDerZahl-(errattungDerZahl/2))
                        if(errattungDerZahl == zufallszahl):
                            gewonnen == True
                            print("Computer hat gewonnen.", "Versuche: ", versuche )
                                if(errattungDerZahl != zufallszahl):
                                    print("Zahl von dem Computer: ", errattungDerZahl)
                                    nichtErraten = input("Wenn die Zufallszahl ist > als die Zahl von dem computer, schreiben Sie 'nein', wenn die Zufallszahl ist < als die Zahl von dem Computer, schreiben Sie 'ja'")
                                    versuche = int(versuche+1)
        