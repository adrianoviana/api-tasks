from flask import Flask, jsonify, request

app = Flask(__name__)

# lista de tarefas
tasks = [
    {'id': 1, 'title': 'Fazer compras', 'done': False},
    {'id': 2, 'title': 'Estudar para a prova', 'done': False}
]

# rota para listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# rota para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# rota para atualizar uma tarefa existente
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

# rota para excluir uma tarefa existente
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
