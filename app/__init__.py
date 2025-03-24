import os
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Ensure the audio directory exists
    static_folder = app.static_folder
    assert static_folder != None
    os.makedirs(os.path.join(static_folder, "audio"), exist_ok=True)

    # Register blueprints
    from app.routes import main

    app.register_blueprint(main)

    return app
