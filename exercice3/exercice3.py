#fonction pour enlever les espaces
def cleanner(txt):
   return " ".join(txt.split())

#demander le nombre de phrase
n = int(input("Combien de phrases souhaitez-vous saisir ? "))

#declarer une liste pour stocker les phrases
phrases = []

for i in range(n):
    phrase = input(f"Saisissez la phrase {i+1}: ")
    phrase = cleanner(phrase)      
    phrases.append(phrase)
    
print("\nVoici les phrases corrigées :")
for phrase in phrases:
    print(phrase)