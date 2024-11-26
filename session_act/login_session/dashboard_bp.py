from flask import Blueprint, render_template, session, redirect, url_for

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/dashboard')
def index():
    if 'username' not in session:
        return redirect(url_for('login.index'))
    return render_template('dashboard.html', username=session['username'])