# les imports inter packages DEVRAIENT être écrits à partir du package
from text_analyser.text_cleaner import Cleaner
# ou à la rigueur en relatif
# from .text_cleaner import Cleaner

class Counter:
    def __init__(self, cleaner: Cleaner, word_length: int=3):
        self.text = cleaner.clean(word_length)

    def count(self, nb_crop: int=5) -> dict:
        occurences = {}
        # transformer le texte néttoyé en dictionnaire d'occurences
        # {"motA": 2, "motB": 3, ...}
        # pour chaque mot du texte,
        #    soit il est pas dans le dictionnaire ==> je l'ajoute avec occurence 1
        #    soit non ==> j'incremente
        for word in self.text.split():
            if word in occurences:
                occurences[word] += 1
            else:
                occurences[word] = 1

        # trier par le dictionnaire par occurence
        # 1. dict -> .items -> list[tuple[key, occcurence]]
        # 2. sorted selon t[1] => occurence (int)
        # 3. reverse=True => décroissant
        # 4. [:nb_crop]: slice des nb_crop premiers
        # 5. dict: reconvertie en dict
        # ne garder que les nb_crop mots les + fréquents
        return dict(sorted(
            occurences.items(), 
            key=lambda t: t[1], 
            reverse=True
        )[:nb_crop])

