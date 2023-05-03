from argparse import ArgumentParser
"""
import random est utilisé pour générer des nombres aléatoires pour des tâches non sensibles, tandis que import secrets est utilisé pour générer des nombres aléatoires cryptographiques pour des tâches de sécurité
"""
import secrets
import random
import string
import pyperclip as pc

# description du script
parser = ArgumentParser(
    prog='Générateur de mot de passe.',
    description='Génère des mots de passe aléatoire personnalisé ou non. Le mot de passe généré est automatiquement copier dans le presse papier.'
)

# ajouter des arguments au script
parser.add_argument("-nb", "--nombre", default=0,
                    help="Nombre de chiffre", type=int)
parser.add_argument("-mi", "--minuscule", default=0,
                    help="Nombre de lettre minuscule", type=int)
parser.add_argument("-ma", "--majuscule", default=0,
                    help="Nombre de lettre majuscule", type=int)
parser.add_argument("-cs", "--caractere-special", default=0,
                    help="Nombre de caractère spécial", type=int)
parser.add_argument("-lg", "--longueur", type=int,
                    help="La longueur totale du mot de passe. S'il est passé, il ignorera -nb, -mi, -ma et -cs, et générer des mots de passe complètement aléatoires avec la longueur spécifiée")
parser.add_argument("-qte", "--quentite", default=1,
                    help="Nombre de mot de passe à générer", type=int)

# on recup la commande
args = parser.parse_args()

# liste qui va contenir le(s) mdp
passwords = []

# boucle pour chaque quantité de mdp (argument quantite)
for _ in range(args.quentite):
    if args.longueur:
        # génère un mot de passe de la longueur entré en argument composé de chiffre, majuscule, minuscule et caratère spécial
        passwords.append("".join(
            [secrets.choice(string.digits + string.ascii_letters + string.punctuation)
                for _ in range(args.longueur)]))
    else:
        password = []
        for _ in range(args.nombre):
            password.append(secrets.choice(string.digits))

        for _ in range(args.majuscule):
            password.append(secrets.choice(string.ascii_majuscule))

        for _ in range(args.minuscule):
            password.append(secrets.choice(string.ascii_minuscule))

        for _ in range(args.caractere_special):
            password.append(secrets.choice(string.punctuation))

        # on mélange les caractères
        random.shuffle(password)

        # on transforme le mdp en chaine de caratère, actuellement en liste
        password = ''.join(password)

        # on ajoute le mdp dans la liste mdp finale
        passwords.append(password)

# copier le ou les mdp généré
pc.copy("\n".join(passwords))

print('\n'.join(passwords))
