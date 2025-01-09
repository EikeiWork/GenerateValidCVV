import time
import os
import random

# Fonction pour afficher le texte ASCII avec un compteur
def display_ascii_art_with_countdown():
    ascii_art = r"""
██████╗ ███████╗███╗   ██╗███████╗██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██████╔╝
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═════╝ 
    """
    orange = "\033[38;5;214m"  # Code ANSI pour l'orange
    reset_color = "\033[0m"
    
    print(f"{orange}{ascii_art}{reset_color}")

    # Compteur de 3 secondes
    for i in range(3, 0, -1):
        print(f"Début de la génération dans {i} secondes...")
        time.sleep(1)

# Fonction pour générer des combinaisons de 16 chiffres dans la plage spécifiée
def generate_combinations(start, end):
    current = start
    while current <= end:
        yield f"{current:016d}"  # Formater pour avoir toujours 16 chiffres
        current += 1  # Incrémenter de 1

# Fonction pour vérifier la validité de la carte
def is_valid_card(card_number):
    sum_odd_digits = 0
    sum_even_digits = 0
    total = 0

    card_number = card_number.replace("-", "").replace(" ", "")[::-1]

    for x in card_number[::2]:
        sum_odd_digits += int(x)

    for x in card_number[1::2]:
        x = int(x) * 2
        if x >= 10:
            sum_even_digits += (1 + (x % 10))
        else:
            sum_even_digits += x

    total = sum_odd_digits + sum_even_digits

    return total % 10 == 0

# Fonction pour générer une date d'expiration valide
def generate_valid_expiration_date():
    month = random.randint(1, 12)  # Mois entre 01 et 12
    year = random.randint(25, 28)    # Année entre 25 et 28
    return f"{month:02}/{year}"

# Fonction pour générer un CVV valide
def generate_valid_cvv():
    return f"{random.randint(1, 999):03}"  # CVV entre 001 et 999

# Utilisation des générateurs
if __name__ == "__main__":
    os.system('')  # Activer l'affichage ANSI sur Windows
    display_ascii_art_with_countdown()  # Affiche l'art ASCII avec le compteur

    start_number = 4540000000000000
    end_number = 5900000000000000
    combo_gen = generate_combinations(start_number, end_number)

    # Affichage des combinaisons valides uniquement
    for combination in combo_gen:
        if is_valid_card(combination):
            expiration_date = generate_valid_expiration_date()
            cvv = generate_valid_cvv()
            print(f"\033[92m{combination}  Exp: {expiration_date}  CVV: {cvv}\033[0m")  # Affiche en vert si valide