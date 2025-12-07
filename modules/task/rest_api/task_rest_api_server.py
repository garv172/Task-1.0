from flask import Blueprint

from modules.task.rest_api.comment_router import CommentRouter
from modules.task.rest_api.task_router import TaskRouter


class TaskRestApiServer:
    @staticmethod
    def create() -> Blueprint:
        task_api_blueprint = Blueprint("task", __name__)
        TaskRouter.create_route(blueprint=task_api_blueprint)
        CommentRouter.create_route(blueprint=task_api_blueprint)
        return task_api_blueprint
