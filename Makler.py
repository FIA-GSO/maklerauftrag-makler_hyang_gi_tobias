
gesamtFläche = 0
raumGröße = {}
weitereRaum = True

while(weitereRaum):
  einzelraum = 0
  gesamtRaum = 0
  quatratisch = str(input("Ist der Raum Quadratisch Ja/Nein "))

  if(quatratisch.lower() == "ja"):
    RaumName = input("Bitte geben Sie den Raumname an ")

    seiteA = float(input("Erste Wand in Metern bis zu 2 Nachkommerstellen "))
    seiteB = float(input("Zweite Wand in Metern bis zu 2 Nachkommerstellen "))
    einzelraum = seiteA * seiteB
    raumGröße[RaumName] = einzelraum
    gesamtFläche = gesamtFläche + einzelraum
    print(raumGröße)
    print(gesamtFläche)
    

  else:
    quadrat = True
    RaumName = input("Bitte geben Sie den Raumname an ")
    print("Teilen sie den Raum bitte in Quadrate auf und geben sie die Maße an")

    while(quadrat == True):
      seiteA = float(input("Erste Wand in Metern bis zu 2 Nachkommerstellen "))
      seiteB = float(input("Zweite Wand in Metern bis zu 2 Nachkommerstellen "))
      einzelraum = seiteA * seiteB
      gesamtRaum = einzelraum + gesamtRaum
      nocheinteil = input("Gibt es noch einen weiteren Teil des Raums? Ja/Nein ")
      if(nocheinteil.lower() == "nein"):
        quadrat = False
        raumGröße[RaumName] = gesamtRaum
        gesamtFläche = gesamtFläche + gesamtRaum
        print(raumGröße)
        print(gesamtFläche)


  
  ende = input("Haben sie noch einen Raum Ja/Nein ")
  if(ende.lower() == "nein"):
    weitereRaum = False
    print(gesamtFläche)
    print(raumGröße)




