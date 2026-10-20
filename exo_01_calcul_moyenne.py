# %%
"""
1/ Expérimentation: dans une cellule individuelle, trouber la fonction interne des str
   qui vérifie si une str est convertible en entier positif, si la str est "numérique" 
1b/ à partir de cette fonction trouver la condition pour également vérifier si une str
   est convertible en entier négatif


2/ saisir n valeurs entiers relatifs dans le clavier séparés par ","


3/ on veut itérer sur les valeurs saisies pour vérifier
   que ces valeurs sont des entiers relatifs (1er cas entier naturel ensuite 2ème cas négatif)

4/ si c'est convertible alors on ajoute la valeur convertie dans une nouvelle liste
4b/ si ce n'est pas convertible => "casser la boucle"

5/ calculer la moyenne arithmétique depuis la liste
6/ présenter le résultat avec 2 chiffres sign. (arrondi en python)
"""

# %%
_str = "-123"
_str.isnumeric()

# if _str.isnumeric():

# int négatif: commence par "-" ET le reste (slice) est numérique
# if _str[0] == "-" and ...
if _str.isnumeric() or (_str.startswith("-") and _str[1:].isnumeric()):
    _str = int(_str)
print(_str)

# %%

values = input("saisir des valueurs entiers relatifs séparés par ,")
print(values)
# %%
values = values.split(",")
print(values)

# %%
for value in values:
    pass
