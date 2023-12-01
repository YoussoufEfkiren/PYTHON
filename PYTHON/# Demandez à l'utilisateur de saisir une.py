# Demandez à l'utilisateur de saisir une phrase
phrase = input("Entrez une phrase : ")

# Utilisez la méthode split() pour diviser la phrase en mots
mots = phrase.split()

# Comptez le nombre de mots
nombre_de_mots = len(mots)

# Affichez le nombre de mots dans la phrase
print(f"La phrase contient {nombre_de_mots} mot(s).")
