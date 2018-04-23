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

for i in range(1,1+runden):
    sieger = ""
    zufallszahl = random.randint(1,6)
    if(zufallszahl ==1 or zufallszahl == 3 or zufallszahl == 5):
        sieger  = "ich"
    else:
        sieger = "Computer"    
    print("Runde", i, "von", i, ": Sieger:", sieger)
