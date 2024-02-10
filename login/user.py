from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from . import database

bp = Blueprint('user', __name__)

@bp.route('/signup')
def sign_up():
    return render_template('signup.html')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = database.get_db()
        user = db.execute(
            "SELECT * FROM USERS WHERE USERNAME = ?", (username, )
        ).fetchone()

        if user:
            flash(f'ユーザー「{username}」はすでに存在しています')
            return redirect(url_for('user.sign_up'))

        db.execute(
            "INSERT INTO USERS (USERNAME, PASSWORD) VALUES (?, ?)",
            (username, generate_password_hash(password))
        )
        db.commit()
        return 'ユーザー登録が完了しました'

    return redirect(url_for('index'))