#fonction pour decouper la phrase
def coupe(txt):
   return txt.split()
#fonction pour assembler
def colle(txt):
   return " ".join(txt)
   
#fonction principal
phrase=input("Entrer une phrase: ")
if phrase.strip()=="":
   print("Veuillez saisir une phrase \n")
else:
   #decouper la phrase
   phrase=coupe(phrase)
   #assembler la phrase
   phrase=colle(phrase)
   print("la phrase devient \n")
   print(phrase)