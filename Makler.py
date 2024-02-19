
gesamtFläche = 0
raumGröße = {}
weitereRaum = True

while(weitereRaum):
  einzelraum = 0
  gesamtRaum = 0
  quatratisch = str(input("Ist der Raum Rechteckig Ja/Nein "))

  if(quatratisch.lower() == "ja"):
    RaumName = input("Bitte geben Sie den Raumname an ")
    try:
      if(RaumName != raumGröße[RaumName]):
        print("Diesen Raum gibt es schon")
    except KeyError:
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
    print("Teilen sie den Raum bitte in Rechtecke auf und geben sie die Maße an")

    try:
      if(RaumName != raumGröße[RaumName]):
        print("Diesen Raum gibt es schon")
    except KeyError:
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




