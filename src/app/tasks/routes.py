from datetime import datetime
from flask import Blueprint, request
from json import loads
from app.common import create_response
from app.models import db, Task, TaskSchema

tasks_bp = Blueprint('tasks_bp', __name__)


@tasks_bp.route('/', methods=['GET'])
def list_tasks():
    tasks = Task.query.order_by(Task.created.desc()).all()
    schema = TaskSchema(many=True)
    output = schema.dump(tasks)
    return create_response(output)


@tasks_bp.route('/', methods=['POST'])
def create_task():
    data = loads(request.data)
    if 'title' in data:
        task = Task(
            title=data['title'],
            created=datetime.now()
        )
        db.session.add(task)
        db.session.commit()
        schema = TaskSchema()
        output = schema.dump(task)
        response = create_response(output, 201)
    else:
        output = {'error': 'The title cannot be null or empty'}
        response = create_response(output, 400)
    return response


@tasks_bp.route('/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.filter(Task.id == task_id).first()
    if task is not None:
        db.session.delete(task)
        db.session.commit()
    return create_response(None, 204)
