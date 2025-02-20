from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/my-route', methods=['GET', 'POST', 'DELETE'])
def my_route():
    return '<h1>Hello!</h1>'


@app.route('/todos', methods=['GET', 'POST'])
def todos():
    response_body = {}
    if request.method == 'GET':
      response_body['results'] = todos
      response_body['message'] = 'Lista de TODOS'
      return response_body, 200
    if request.method == 'POST':
      data = request.json
      if data == {}:
        response_body['message'] = 'ERROR: TODO vacío'
        response_body['results'] = {}
        return response_body, 403
      todos.append(data)
      response_body['message'] = 'TODO agregado con éxito'
      response_body['results'] = todos
      return response_body, 201
       

@app.route('/todos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def todo(id):
    response_body = {}
    if request.method == 'GET':
        response_body['message'] = f'Datos del todo {id}'
        response_body['results'] = {'label': 'todos'}
        return response_body, 200
    if request.method == 'PUT':
        response_body['message'] = f'Actualización del todo {id}'
        response_body['results'] = {'label': 'todos'}
        return response_body, 200
    if request.method == 'DELETE':
        response_body['message'] = f'todo {id} eliminado'
        response_body['results'] = {}
        return response_body, 200


some_data = { 'name': 'Bobby', 'lastname': 'Rixer'}
todos = [ { 'label': 'My first task', 'done': False}]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)