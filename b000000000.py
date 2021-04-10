# -*- coding: utf-8 -*-
"""

@author: zackto
"""

import json

def charge(fichier):
   with open(fichier) as f:
      return json.load(f)

import mysqlx

session = mysqlx.get_session({
    "host": "localhost",
    "port": 33060,
    "user": "root",
    "password": "password"
})

db = session.get_schema("world_x")

def lecture(fichier):

  # Le nom de la collection temporaire
  nomColl = "temp"

  # Crée la collection temporaire maColl
  maColl = db.create_collection(nomColl)

  # charge le fichier dans la variable json
  json = charge(fichier)
    
  # Ajoute le contenu du fichier json dans la collection temporaire maColl
  maColl.add(json).execute()

  # Lis toute les documents convertis de la collection et les stocker dans la variable docs
  docs = maColl.find().execute()

  # Détruit la collection temporaire
  db.drop_collection(nomColl)

  # Retourne un dictionnaire Python du fichier json converti
  return docs

def main():
  docs = lecture('b000000000.json')
  print(len(docs.fetch_all()))


  # Ne pas oublier de remercier le gestionnaire de BD
  session.close



  if __name__== "__main__":
      main()
