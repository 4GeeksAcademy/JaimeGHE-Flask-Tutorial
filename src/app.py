from flask import Flask, jsonify, request


app = Flask(__name__)

todos = [{'label': 'My first task', 'done': False}]

@app.route('/my-route', methods=['GET', 'POST', 'DELETE'])
def my_route():
    return '<h1>Hello!</h1>'

@app.route('/todos', methods=['GET', 'POST'])
def handle_todos():
    response_body = {}
    if request.method == 'GET':
        response_body['results'] = todos
        response_body['message'] = 'Lista de TODOS'
        return response_body, 200
    if request.method == 'POST':
        data = request.json
        if not data:
            response_body['message'] = 'ERROR: TODO vacío'
            response_body['results'] = {}
            return response_body, 403
        todos.append(data)
        response_body['message'] = 'TODO agregado con éxito'
        response_body['results'] = todos
        return response_body, 201

@app.route('/todos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_todo_by_id(id):
    response_body = {}
    if request.method == 'GET':
        if id < len(todos):
            response_body['message'] = f'Datos del todo {id}'
            response_body['results'] = todos[id]
            return response_body, 200
        else:
            response_body['message'] = 'TODO no encontrado'
            response_body['results'] = {}
            return response_body, 404
    if request.method == 'PUT':
        data = request.json
        if id < len(todos):
            todos[id] = data
            response_body['message'] = f'Actualización del todo {id}'
            response_body['results'] = todos[id]
            return response_body, 200
        else:
            response_body['message'] = 'TODO no encontrado'
            response_body['results'] = {}
            return response_body, 404
    if request.method == 'DELETE':
        if id < len(todos):
            deleted_todo = todos.pop(id)
            response_body['message'] = f'TODO {id} eliminado'
            response_body['results'] = deleted_todo
            return response_body, 200
        else:
            response_body['message'] = 'TODO no encontrado'
            response_body['results'] = {}
            return response_body, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
