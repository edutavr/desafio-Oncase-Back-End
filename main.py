import os
import json

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from db import Formularios

idx = 6

app = Flask(__name__)
app.json.sort_keys = False

def salvar(data):
    with open('db.py', 'w') as db_file:
        db_file.write(f"Formularios = {json.dumps(data, indent=4)}")

@app.route('/formularios',methods=['GET'])
@cross_origin()
def get():
    return make_response(
        jsonify(Formularios)
    )



@app.route('/formularios',methods=['POST'])
@cross_origin()
def post():
    data = request.json
    data['id'] = globals()['idx']
    globals()['idx']+=1
    Formularios.append(data)
    salvar(Formularios)
    return make_response(
        jsonify(data)
    )
    


app.run()