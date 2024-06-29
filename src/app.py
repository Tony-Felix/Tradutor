from flask import Flask

from controllers.admin_controller import admin_controller
from controllers.render_template_controller import render_template_controller
from controllers.list_controller import list_controller

from os import environ
from waitress import serve


app = Flask(__name__)
app.template_folder = "views/templates"
app.static_folder = "views/static"

app.register_blueprint(admin_controller, url_prefix="/admin")
app.register_blueprint(render_template_controller, url_prefix="/")
app.register_blueprint(list_controller, url_prefix="/history")


def start_server(host="0.0.0.0", port=8000):
    if environ.get("FLASK_ENV") != "production":
        return app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
