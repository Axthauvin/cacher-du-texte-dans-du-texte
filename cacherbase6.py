def base6(nombre):
    """
    renvoie le nombre en base 6 codé sur '4 bits'
    """
    if nombre >= 6**4:
        return "Erreur"
    Base6 = [0, 0, 0, 0]
    while nombre > 0:
        Base6[3] = Base6[3] + 1
        nombre -= 1
        if int(Base6[3]) >= 6:
            Base6[3] = 0
            Base6[2] = Base6[2] + 1
        if int(Base6[2]) >= 6:
            Base6[2] = 0
            Base6[1] = Base6[1] + 1
        if int(Base6[1]) >= 6:
            Base6[1] = 0
            Base6[0] = Base6[0] + 1
    #print(Base6)

    base6str = ""
    for el in Base6:
        base6str += str(el)

    return base6str
        

def CacherMessage(original, acacher):
    original = original[:-1] + original[-1] 
    acacher = acacher[:-1] + acacher[-1] 
    print("longeur de original", len(original))
    print("longeur de acacher", len(acacher))
    
    if len(original) < len(acacher) * 4:
        return "Erreur ! Le message original est trop court ! Il a besoin de " + str(len(acacher) * 4) + " caractères. \nSoit " + str(len(acacher) * 4 - len(original)) + " de plus.\n Ou on peut aussi raccoucir le message caché de " + str(len(acacher) - int(len(original) / 4)) +  " lettres."
    listeBase2 = []
    for lettre in acacher:
        binary = base6(ord(lettre))
        if binary == "Erreur":
            return "Le caractère " + lettre + " est trop loin dans la table UTF-8" 

        listeBase2.append(binary)
    #print(listeBase2)

    possibilites = ["", "\u200C", "\u200D", "\u200E", "\u200F", "\u034F"]
    
    chaineFinale = ""
    compteur = 0
    for binaires in listeBase2:
        for unbit in binaires:
            chaineFinale += original[compteur]
            if int(unbit) > 0:
                chaineFinale += possibilites[int(unbit)]
            compteur += 1
    
    chaineFinale += original[compteur:]
    print("Longeur du message initial", len(original))
    print("Longeur du message avec le message caché", len(chaineFinale))

    

    return chaineFinale
    


#message = CacherMessage("Je suis Axel, un programmeur. Je suis même auto-entrepreneur ! Je dois faire un message très long afin de cacher mon texte dans du texte", "Bonjour richard")

def decodeMessage(message):
    listebinaire = []
    binaire = ""
    caractere = 1
    possibilites = ["", "\u200C", "\u200D", "\u200E", "\u200F", "\u034F"]
    while caractere < len(message):
        
        
        
        if message[caractere] in possibilites:
            binaire += str(possibilites.index(message[caractere]))
            
        else:
            binaire += "0"
            caractere -= 1
        
        caractere += 2
        
        

        if len(binaire) == 4 and binaire != "0000":
            listebinaire.append(binaire)
            binaire = ""
    
    strfinale = ""
    for lettre in listebinaire:
        strfinale += chr(int(lettre, 6))
    
    return strfinale

        
#print(decodeMessage(message))

"""
c1 = 'ax'
c2 = 'el'

print(c1 + '\u001d' + c2)
"""

