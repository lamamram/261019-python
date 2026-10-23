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

# %% -------------- gestion dynamique des attributs: getattr, setattr, hasattr -------------------

class Truc:
    pass

t = Truc()

print(f"est que l'objet t a un attribut du nom 'param' ? {hasattr(t, "param")}")
setattr(t, "param", 10)
# print(f"et maintenant ? {hasattr(t, "param")} et c'est {t.param}")
print(f"et maintenant ? {hasattr(t, "param")} et c'est {getattr(t, "param")}")


# %% ------------------ créer un client d'api pour gorest.co.in --------------
import requests
from typing import List, Mapping, Any

class GoRestApiV2:
    def __init__(self):
        self.path = "https://gorest.co.in/public" 
        self.version = "v2"

    def __call(self, method: str, endpoint: str):
        ret = {"data": [], "error": ""}
        try:
            url = self.path + "/" + self.version + "/" + endpoint
            call_fn = getattr(requests, method.lower())
            r = call_fn(url)

            if 200 <= r.status_code < 300:
                if "application/json" in r.headers["content-type"]:
                    ret["data"] = r.json()

            else:
                raise ValueError(f"mauvais code: {r.status_code}")
        except (requests.ConnectionError, ValueError) as e:
            ret["error"]
        return ret
            

    def get_users(self, per_page: int=100) -> Mapping[str, Any]:
        """retourne tous les utilisateurs !!!"""
        i = 1
        data = []
        while True:
            ret = self.__call("GET", f"users?per_page={per_page}&page={i}")
            if ret["error"]:
                raise ValueError(ret["error"])
            # le serveur retourne [] quand il n'ya plus de données
            elif not ret["data"]:
                break
            print(f"page {i} fetched !")
            data += ret["data"]
            i += 1
        ret["data"] = data
        return ret

    def get_user(self, user_id: int):
        return self.__call("GET", f"users/{user_id}")
        


api = GoRestApiV2()
api.get_users()
# api.get_user(8331323)

# %%
