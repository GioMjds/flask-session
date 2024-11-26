from flask import Flask

def create_app():
    app = Flask(__name__)

    app.secret_key = 'Mimicplays12'

    from session_act.login_session.login_bp import login
    from session_act.login_session.dashboard_bp import dashboard

    app.register_blueprint(login)
    app.register_blueprint(dashboard)

    return app