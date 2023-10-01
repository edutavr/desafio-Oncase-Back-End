import json

Formularios = [ 
  {
    "id": 1,
    "firstname": "Carlos",
    "lastname": "Moura",
    "percentage": 5
  },
  {
    "id": 2,
    "firstname": "Fernanda",
    "lastname": "Oliveira",
    "percentage": 15
  },
  {
    "id": 3,
    "firstname": "Hugo ",
    "lastname": "Silva",
    "percentage": 20
  },
  {
    "id": 4,
    "firstname": "Eliza",
    "lastname": "Souza",
    "percentage": 20
  },
  {
    "id": 5,
    "firstname": "Anderson",
    "lastname": "Santos",
    "percentage": 40
  }
]

def salvar(data):
    with open('dados.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)