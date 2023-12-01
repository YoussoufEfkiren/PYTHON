# Demander à l'utilisateur d'entrer son âge
age = int(input("Entrez votre âge : "))

# Définir un dictionnaire de catégories d'âge
categories_age = {
    (1, 17): "mineur",
    (18, 70): "adulte",
    (71, float('inf')): "âgé"
}

# Parcourir le dictionnaire et déterminer la catégorie d'âge
categorie = None
for (min_age, max_age), cat in categories_age.items():
    if min_age <= age < max_age:
        categorie = cat
        break

# Afficher la catégorie
if categorie:
    print("Vous êtes considéré comme un(e)", categorie)
else:
    print("Âge invalide.")


