import random

def jeu_devinette():
    print("Bienvenue dans le jeu de devinette !")
    print("Je pense à un nombre entre 1 et 100.")
    
    nombre_secret = random.randint(1, 100)
    tentatives = 0
    trouve = False
    
    while not trouve:
        try:
            essai = int(input("Entrez votre proposition : "))
            tentatives += 1
            
            if essai < nombre_secret:
                print("C'est plus grand !")
            elif essai > nombre_secret:
                print("C'est plus petit !")
            else:
                print(f"Bravo ! Vous avez trouvé en {tentatives} tentative(s).")
                trouve = True
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    print("Merci d'avoir joué !")

if __name__ == "__main__":
    jeu_devinette()