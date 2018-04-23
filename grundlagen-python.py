# Grundlagen-python.py
import random
# Kommentare erfolgen mit hashtag

# Ausgabe von Daten 
print("Hallo World")

# Variable definieren(kann ohne typ erfolgen)
heimat = "Erde"

# Mehrere Variable werden mit , getrennt
print(heimat, "an World: ", "Hallo")

#Eingabe/ liest Text von der Console ein
wer  = input("Und wer bist du? ")

# und gibt den Text wieder aus
if(wer == "ich"):
    print("Hallo Du!") 
else:
    print("Hallo" , wer)

lieblingszahl = input("Was ist deine Lieblingszahl?")
print("Super, ich mag die Zahl ", lieblingszahl)
print("Aber die coolere Zahl ", int (lieblingszahl)+10, "mag ich noch mehr!!!")

runden = input("Wie viele Runden sollen wir spielen? ")
runden = int(runden)

for i in range(1, runden+1): 
    gewinnIch = 0
    gewinnComputer = 0
    sieger = ""
    zufallszahl = random.randint(1,6)
    if(zufallszahl ==1 or zufallszahl == 3 or zufallszahl == 5):
        sieger  = "ich"
        gewinnIch = int(gewinnIch+1)
    else:
        sieger = "Computer"    
        gewinnComputer = int(gewinnComputer+1)
    print("Runde", i, "von", runden, ": Sieger:", sieger,": gewuerfelt wurde: ", zufallszahl)
if(gewinnIch==gewinnComputer):
        print("Unentschieden")
if(gewinnComputer>gewinnIch):
        print("Computer hat gewonnen")
if(gewinnIch>gewinnComputer):
        print("Ich habe gewonnen")    
print("game over")
