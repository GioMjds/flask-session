from flask import Blueprint, render_template, request, redirect, url_for, session, flash

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
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@login.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login.index'))