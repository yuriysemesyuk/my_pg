from app import app, db
from flask import render_template, request, flash, redirect, url_for
from forms import RegistrationForm
from models import User
from flask_security.core import current_user


@app.route('/')
def index():
    if current_user:
        return redirect('/user_page')
    return redirect(url_for('security.login'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(login=form.login.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('security.login'))
    return render_template('register.html', form=form)