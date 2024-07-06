# liste des mois en français

listmois={
    "fr":[
    "Janvier", "Février", "Mars",
    "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre",
    "Octobre", "Novembre", "Décembre"],
    "en":[
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"]
}


# Fonction pour afficher les mois
def afficher_mois(langue='fr'):
    mois=listmois[langue]
    
    # Affichage des mois en trois colonnes
    for i in range(0,3):
        for j in range(0,4):
            print(f"{mois[i+3*j]:15}", end=" ")
        print()
         
        

# Menu pour les choix
def menu():
     while True:
        choix = input("""
    Menu de choix :
    f - Français
    a - Anglais
    Entrez votre choix : """).strip().lower()
        if choix == 'a':
            afficher_mois('en')
            break
        else:
            if choix != "f":
                print("\nChoix invalide, Affichage en Français \n")
            afficher_mois()
            break
       
           
# Programme principal
verif=True
while verif:
    menu()
    continuer = input("\nVoulez-vous continuer ? (o/n) : ").strip().lower()
    if continuer != 'o':
        verif=False
        print("Programme terminé.")
        break
