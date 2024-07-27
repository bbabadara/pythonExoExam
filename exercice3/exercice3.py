#fonction pour enlever les espaces
def cleanner(txt):
   return " ".join(txt.split())

#fonction pour verifier si la phrase se termine par un point
def verifpoint(phrase):
    if phrase[-1] == ".":
        return True    
    return False
        
#demander le nombre de phrase
n = int(input("Combien de phrases souhaitez-vous saisir ? "))

#declarer une liste pour stocker les phrases
phrases = []

for i in range(n):
    phrase = input(f"Saisissez la phrase {i+1}: ")
    phrases.append(phrase)
    
print("\nVoici les phrases corrigées :")
for phrase in phrases:
    print(phrase)