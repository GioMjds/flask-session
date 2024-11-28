from flask import Blueprint, render_template, request, redirect, url_for, session, make_response

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return redirect(url_for('dashboard.index'))
    
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username and password:
            session['username'] = username
            return redirect(url_for('dashboard.index'))

    response = make_response(render_template('login.html'))
    response.headers['Cache-Control'] = 'no-store'
    return response

@login.route('/logout')
def logout():
    session.pop('username', None)
    response = make_response(redirect(url_for('login.index')))
    response.headers['Cache-Control'] = 'no-store'
    return response