
raumGroeßen = []
weitereRaum = True
raumGibtes = False


# Raum Form berechen

def rechteck(rekEins, rekzwei):
  raumMaße = rekEins * rekzwei
  return raumMaße
   
def multiquadrat(maßeArray):
  gesamtFläsche = 0
  for element in maßeArray:
    einzelquadrat = element[0] * element[1]
    gesamtFläsche = gesamtFläsche + einzelquadrat
  return gesamtFläsche

def dreieckig(AnKat, geKat):
  # Gilt nur für Rechtwinklig
  raumMaße = (AnKat * geKat) / 2
  return raumMaße

# 

while(weitereRaum):
  
  # Überprüfen ob es den Raum gibt
    
  RaumName = input("Bitte geben Sie den Raumname an: ")
  
  if(raumGroeßen != []):
    for element in raumGroeßen:
      if RaumName == element[0]:
        print('Raum Gibt es schon')
        raumGibtes = True
      else:
        print("fine")
        raumGibtes = False
        
  
  if(raumGibtes == False):
    
    # Einzel Reckteck Raum
    
    rechteckig = str(input("Welche Form hat der Raum R = Rechteckig M = Mehrere Rechtecke D = Dreieckig: "))
    
    if(rechteckig.lower() == "r"):
      seiteA = float(input("Erste Wand in Metern bis zu 2 Nachkommerstellen: "))
      seiteB = float(input("Zweite Wand in Metern bis zu 2 Nachkommerstellen: "))
      raumGroeßen.append([RaumName, rechteck(seiteA, seiteB)])
      
    # Mehrer Reckecke (sowas wie eine L form Raum)
    
    if(rechteckig.lower() == "m"):
      nocheinTeil = True
      
      maßeArray = []
      while(nocheinTeil == True):
        
        seiteA = float(input("Erste Wand in Metern bis zu 2 Nachkommerstellen: "))
        seiteB = float(input("Zweite Wand in Metern bis zu 2 Nachkommerstellen: "))
        maßeArray.append([seiteA, seiteB])
        
        nocheinteil = str(input("Gibt es noch einen weiteren Teil des Raums? Y/N: "))
        if(nocheinteil.lower() != "ja"):
          nocheinTeil = False
          raumGroeßen.append([RaumName, multiquadrat(maßeArray)])
          print(raumGroeßen)
          
    # Dreieckiger Raum
    
    if(rechteckig.lower() == "d"):
      seiteA = float(input("Erste Wand (Ankatete) in Metern bis zu 2 Nachkommerstellen: "))
      seiteB = float(input("Zweite Wand (Gegenkatete) in Metern bis zu 2 Nachkommerstellen: "))        
      raumGroeßen.append([RaumName, dreieckig(seiteA, seiteB)])
      
    # Noch ein Raum abfrage 
    
    nocheinRaum = str(input("Gibt es noch ein Raum Y/N: "))
    
    if(nocheinRaum.lower() == "n"):
      weitereRaum = False
      print(f"Die Raum maße sind {raumGroeßen}.")
      gesamtfläsche = 0
      for element in raumGroeßen:
        gesamtfläsche = gesamtfläsche + element[1]
        
      print(f"Die Gesamt Fläsche ist {gesamtfläsche}m.")
          

        

        
    
    