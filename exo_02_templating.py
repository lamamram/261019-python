# %%
"""
exercice : remplacer les clés entourées par "((" et "))"
dans un texte par les valeurs correspondantes dans un dico

1. afficher le contenu entre la première occurence de (( et ))
2. remplacer ((pression)) par 500 dans _template
Hint: regarder la fonction str.replace
3. itérer sur _template pour remplacer toutes les slots (())
par la clé correspondante si celle ci existe ou par N/A
"""

_template = """
robinet.pression=((pression))
robinet.section=((section))
robinet.debit=((debit))
robinet.capacite=((capacite))
"""

injections = {
    "pression": 500,
    "section": 30,
    "debit": 2
}

# %%
start_index = _template.index("((") + 2
end_index = _template.index("))")
key = _template[start_index:end_index]

to_replace = "((" + key + "))"
real_value = str(injections[key])

print(_template.replace(to_replace, real_value))

# %%
_str = "remplacer un truc dans une phrase"
print(_str.replace("truc", "machin"))

# %% ------------------- tentative avec for --------------------

for key in injections:
    _template = _template.replace("((" + key + "))", str(injections[key]))

print(_template)

# %% ---------------------- avec while ------------------------

while "((" in _template:
    start_index = _template.index("((") + 2
    end_index = _template.index("))")
    key = _template[start_index:end_index]

    to_replace = "((" + key + "))"
    real_value = str(injections.get(key, "N/A"))

    _template = _template.replace(to_replace, real_value)

print(_template)


# %% ----- portage de la cellule précédente en fonction ----------
"""
technique
1/ entourer le code avec l'entête de def et ajouter le nom
2/ transformer le print ou affectation finale en return
3/ réféchir sur les paramètres d'entrée (positionnels / centraux, et optionnels => valeur par défaut) et de sortie
4/ refactorer le code pour utiliser les paramètres d'entrée et construire la sortie
5/ tester dans différents cas
   1. le cas de l'exemple
   2. le cas ci dessous
"""

def parse_template(
        tpl: str, 
        data: dict, 
        delimiters: tuple = ("{{", "}}"), 
        default: str = "N/A",
        **opts
    ) -> str:
    """
    fonction d'injection de données dans un template
    
    options avancées:

    debug=True : active le mode debuggage
    """
    while delimiters[0] in tpl:
        start_index = tpl.index(delimiters[0]) + len(delimiters[0])
        end_index = tpl.index(delimiters[1])
        key = tpl[start_index:end_index]
        if "debug" in opts and opts["debug"] == True:
            print(f"DEBUG: detected key: {key}") 

        to_replace = delimiters[0] + key + delimiters[1]
        real_value = str(data.get(key, default))

        tpl = tpl.replace(to_replace, real_value)

    return tpl


print(parse_template(_template, injections, delimiters=("((","))")))

t = """blabla {{param}}"""
data = {"param": 100}

print(parse_template(t, data, debug=True))


# %%
