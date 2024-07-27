import re

def est_valide(numero):

    # Supprime les espaces
    numero = numero.replace(" ", "")
    
    # Vérifie la longueur après suppression des espaces
    if len(numero) != 9:
        return False
    
    # Vérifie le début du numéro
    if not numero.startswith(('77', '78', '76', '70', '75')):
        return False
    
    # Vérifie que le reste du numéro est bien numérique
    return numero.isdigit()

def classer_numeros(chaine):
    # Expression régulière pour extraire les numéros
    numeros = re.findall(r'\b\d+\b', chaine)
    
    valides = []
    invalides = []
    
    for numero in numeros:
        if est_valide(numero):
            valides.append(numero)
        else:
            invalides.append(numero)
    
    return valides, invalides

def compter_operateurs(numeros):
    
    compte = {
        '77': 0,
        '78': 0,
        '76': 0,
        '70': 0,
        '75': 0
    }
    
    for numero in numeros:
        prefixe = numero[:2]
        if prefixe in compte:
            compte[prefixe] += 1
    
    return compte

def afficher_resultats(valides, invalides):
    print("Numéros valides :")
    for numero in valides:
        print(f"  {numero}")
    
    print("\nNuméros invalides :")
    for numero in invalides:
        print(f"  {numero}")
    
    # Comptage et affichage des opérateurs
    compte = compter_operateurs(valides)
    
    print("\nNombre de numéros par opérateur :")
    for operateur, nombre in compte.items():
        print(f"  {operateur} : {nombre}")

def main():
    # Lecture de la chaîne de saisie
    chaine = input("Entrez la chaîne de numéros : ")
    
    if not chaine.strip():
        print("La chaîne de saisie est obligatoire.")
        return
    
    valides, invalides = classer_numeros(chaine)
    afficher_resultats(valides, invalides)

main()
