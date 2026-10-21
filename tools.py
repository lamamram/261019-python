DEBUG = False

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

print("coucou")