# %%
"""
exemple d'appel d'api REST en GET sur un endpoint /users du domaine gorest.co.in
REST: Representational State Transfer
méthode de communication entre un client et un serveur via HTTP
utlisant les méthodes HTTP standard comme POST, GET, PUT, DELETE
pour effectuer des opérations       CRUD Create,Read,Update,Delete) sur les ressources du serveur
les ressources sont identifiées par des URI (Uniform Resource Identifier)
/posts, /users, /comments
en majorité, les données d'entrées et de sortie sont des objets JSON
"""

import requests

URL = "https://gorest.co.in/public/v2/users"

try:
    r = requests.get(URL)

    if 200 <= r.status_code < 300:
        if "application/json" in r.headers["content-type"]:
            data = r.json()
    else:
        raise ValueError(f"mauvais code: {r.status_code}")
except (requests.ConnectionError, ValueError) as e:
    print(e)

print(data)
# %%
