# liste des mois en français
m_fr = [
    "Janvier", "Février", "Mars",
    "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre",
    "Octobre", "Novembre", "Décembre"
]

# liste des mois en anglais
m_en = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]

# Fonction pour afficher les mois
def afficher_mois(langue='fr'):
    if langue == 'fr':
        mois = m_fr
    elif langue == 'en':
        mois = m_en
    else:
        print("Saisie incorrert. Affichage en Français.")
        mois = m_fr
    
    # Affichage des mois en trois colonnes
    for i in range(1, 13):
         print(mois[i-1].ljust(15), end=" ")
         if i%3==0:
            print("\n")

# Menu pour les choix
def menu():
     while True:
        choix = input("""
    Menu de choix :
    f - Français
    a - Anglais
    Entrez votre choix : """).strip().lower()
        if choix == 'f':
            afficher_mois('fr')
            break
        elif choix == 'a':
            afficher_mois('en')
            break
        else:
            print("Choix non reconnu. Veuillez entrer 'f' ou 'a'.")
           
# Programme principal
verif=True
while verif:
    menu()
    continuer = input("\nVoulez-vous continuer ? (o/n) : ").strip().lower()
    if continuer != 'o':
        verif=False
        print("Programme terminé.")
        break
