from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

tasks = [
    "Study",
    "Work",
    "Exercise",
    "Cooking",
    "Meditation",
    ]

task_data = {task: 0 for task in tasks}

@app.route('/')
def hello():
    return render_template("layout.html", tasks=tasks)

@app.route('/complete_task', methods=['POST'])
def complete_task():
    task_name = request.json.get('task')
    if task_name in task_data:
        task_data[task_name] += 1 
        return jsonify(success=True, count=task_data[task_name])
    return jsonify(success=False, message="Task not found"), 404