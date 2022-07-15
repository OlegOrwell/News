from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "something awesome"

    from website.views import views
    app.register_blueprint(views)
    return app