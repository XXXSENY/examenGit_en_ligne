# Fonction 1 : addition
def addition(a, b):
    return a + b

# Fonction 2 : soustraction
def soustraction(a, b):
    return a - b

# Fonction 3 : multiplication
def multiplication(a, b):
    return a * b

# Fonction 4 : division
def division(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

# Fonction 5 : puissance
def puissance(base, exposant):
    return base ** exposant

# Fonction 6 : factorielle (récursive)
def factorielle(n):
    if n < 0:
        return "Erreur : nombre négatif"
    if n == 0 or n == 1:
        return 1
    return n * factorielle(n - 1)

# Fonction 7 : vérifier si un nombre est pair
def est_pair(n):
    return n % 2 == 0

# Fonction 8 : renverser une chaîne de caractères
def renverser_chaine(chaine):
    return chaine[::-1]

# Fonction 9 : compter les voyelles dans une chaîne
def compter_voyelles(texte):
    voyelles = "aeiouyAEIOUY"
    return sum(1 for char in texte if char in voyelles)

# Fonction 10 : convertir des degrés Celsius en Fahrenheit
def celsius_vers_fahrenheit(celsius):
    return (celsius * 9/5) + 32