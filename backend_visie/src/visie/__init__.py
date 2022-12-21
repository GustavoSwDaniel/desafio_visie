from flask import Flask
from flask_cors import CORS
from src.config import Config
from src.exception import RepositoryException, DataNotFoundException
from src.handlers import bad_request_exception_handler, not_found_exception_handler
from src.visie.infrastructure.database.database_sql import Database

db = Database(database_url=Config.DATABASE_URL)
cors = CORS()


def create_app() -> Flask:
    app = Flask(__name__)
    cors.init_app(app)

    from src.visie.people import bp as people_bp
    app.register_blueprint(people_bp)

    app.register_error_handler(RepositoryException, bad_request_exception_handler)
    app.register_error_handler(DataNotFoundException, not_found_exception_handler)

    return app
