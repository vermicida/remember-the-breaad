from . import db, ma


class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    title = db.Column(
        db.String(256),
        index=False,
        unique=False,
        nullable=False
    )

    created = db.Column(
        db.DateTime,
        index=True,
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return f'<Task {self.id}, {self.title}>'


class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task
