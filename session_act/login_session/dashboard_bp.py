from flask import Blueprint, render_template, session, redirect, url_for, make_response

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/dashboard')
def index():
    if 'username' not in session:
        response = make_response(redirect(url_for('login.index')))
        response.headers['Cache-Control'] = 'no-store'
        return response

    response = make_response(render_template('dashboard.html', username=session['username']))
    response.headers['Cache-Control'] = 'no-store'
    return response