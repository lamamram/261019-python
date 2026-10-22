# %%
"""

URL: https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip
outils: pip install requests

1. téléchargement en GET et en binaire

2. extraire le fichier .csv contenu dans le zip à télécharger
hint: zipfile.Zipfile (doc ou google/stackoverflow)
hint: les zip s'ouvrent et se ferment
hint: pour trouver le nom du fichier à extraire regarder la méthode .namelist() de l'objet ZipFile

3. déplacer le fichier csv en dans data/dns.csv
4. ne faire ce qui précède qui si ce n'est pas déjà fait
hint: module os et pathlib.Path


5. écrire un script qui
- extrait n=2 paquets de nb_line=100000 lignes de donnée, sans le header
- à chaque paquet de lignes, faire les opérations suivantes:
   - créé un nouveau fichier csv à nommer en fct du nb de ligne
   - insère le header dans ce nouveau fichier
   - écrit le paquet de lignes

modus operandi: faire ceci en n'ouvrant le csv en lecture qu'une seule fois
"""
# attendre xs avant de continuer
from time import sleep

# %% -------------------------- téléchargement avec requests -------------------------------

"""
HTTP: Hyper Text Transfer Protocl

protocole d'échange de données entre un client (requête HTTP) et un serveur distant qui délivre une réponse HTTP

requête HTTP
--------------
- version de http (1.1) / 2 / 3
- URL : Unified Resource Location: adresse d'une ressource 
protocole|://|nom de domaine|chemin(path) physique ou virtuel|resource (.html, .php, .zip, ...)          |query parameters    |hash données supplémentaires
https     :// www.afnic.fr  |/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip|?param=1&param2=truc|#tag

- Méthode ou verbe HTTP: mode d'accès à la ressource
  GET: lire la ressource
  POST: créer la ressource sur le serveur distant (formulaire)
  PUT/PATCH : modifier la ressource complètement ou partiellement
  DELETE: supprimer la ressource distante

- les entêtes de requêtes : métadonnées (infos contextuelles sur le client)

- données de la requête en cas de POST/PUT/PATCH


Réponse HTTP
------------

                                                     OK  | OK mais redirection| pb sur la requête| pb serveur
- Code de statut: entier répartie en famille de code 2XX | 3XX                | 4XX              | 5XX
- entête de réponse: infos sur le serveur
- le corps de la réponse (html, fichier sous forme de flux d'octets, json ... )
"""

# %%

import requests
from urllib.parse import urlsplit
import os
from pathlib import Path


URL = "https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
archive_name = urlsplit(URL).path
archive_name = os.path.split(archive_name)[-1]
# archive_name = URL.split("/")[-1]

p_archive = Path(f"./{archive_name}")
# si l'on a pas déjà téléchargé l'archive

# if not os.path.exists():
if not p_archive.exists():
# le réseau indépendant de notre volonté ==> try
   try:
      r = requests.get(URL)

      # 1. regarder le status_code
      if 200 <= r.status_code < 300:
         # 2. regarder le type de contenu i.e l'entête Content-Type dans les entêtes
         if "application/zip" in r.headers["content-type"]:
            # 3. selectionner le bon corps de réponse
            # ---------------------------------> binaire
            with open(f"./{archive_name}", mode="wb") as f:
               f.write(r.content)
      else:
         raise ValueError(f"mauvais code: {r.status_code}")
   except (requests.ConnectionError, ValueError) as e:
      print(e)





# %% -------------------- décompresser une archive ----------------------
# rendre la cellule idempotente (même puissance => même état finale qq soit le nb d'exécution)
from zipfile import ZipFile

p_data = Path("./data")
p_dns = p_data / "dns.csv"

# print(p_dns)
# print(p_dns.absolute())

# if not os.path.exists("./data/dns.csv"):
if not p_dns.exists():
   with ZipFile(p_archive, mode="r") as z:
      csv_name = z.namelist()[0]
      z.extract(csv_name)

   if not p_data.exists():
      os.mkdir(p_data)
   os.rename(f"./{csv_name}", p_dns)

# %%
