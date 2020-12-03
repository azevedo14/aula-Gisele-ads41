from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request, Flask, render_template
from app import app
from app import mongo
from classe import Celular

@app.route('/')
def index():
    return "N3 Vinicius Azevedo / ADS - 41"

@app.route('/adicionar', methods=['POST'])
def add_celular():

    _json = request.json
    celular = Celular(_json["modelo"], _json["marca"], _json["cor"])

    if celular.modelo and celular.marca and celular.cor and request.method == 'POST':

        id = mongo.db.smart.insert(
            {'modelo': celular.modelo, 'marca': celular.marca, 'cor': celular.cor})

        resp = jsonify("Cadastro de celular adicionado")

        resp.status_code = 200

        return resp


@app.route('/list')
def listar_celular():
    celular = mongo.db.smart.find()
    resp = dumps(celular)
    return resp


@app.route('/smart/<id>')
def pesquisar_celular(id):
    celular = mongo.db.smart.find_one({'_id': ObjectId(id)})
    resp = dumps(celular)
    return resp


@app.route('/delete/<id>', methods=['DELETE'])
def delete_celular(id):
    mongo.db.smart.delete_one({'_id': ObjectId(id)})
    resp = jsonify("Cadastro de celular deletado")

    resp.status_code = 200

    return resp


@app.route('/update/<id>', methods=['PUT'])
def update_celular(id):
    _id = id
    _json = request.json
    celular = Celular(_json["modelo"], _json["marca"], _json["cor"])


    if celular.modelo and celular.marca and celular.cor and _id and request.method == 'PUT':

        mongo.db.smart.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(
            _id)}, {'$set': {'modelo': celular.modelo, 'marca': celular.marca, 'cor': celular.cor}})

        resp = jsonify("Cadastro de celular atualizado")

        resp.status_code = 200

        return resp


if __name__ == "__main__":
    app.run(debug=True)
