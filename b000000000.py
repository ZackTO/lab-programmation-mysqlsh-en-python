# -*- coding: utf-8 -*-
"""

@author: zackto
"""

import json

def charge(fichier):
   with open(fichier) as f:
      return json.load(f)

def main():
  #print(charge('b000000000.json'))

  if __name__== "__main__":
      main()
