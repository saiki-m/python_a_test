from flask import Blueprint, render_template, session, redirect, url_for, flash
from forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required
from models import db, User

##############
# app.pyのルーティングを分割。ログイン、ログアウト、新規登録、登録完了があります。
##############

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


#ログイン
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()      #forms.pyのLoginFormクラスからオブジェクトを作る
    # POST
    if loginform.validate_on_submit():    #validatorが表示されないなら、  
        # データ入力取得
        username = loginform.name.data
        password = loginform.password.data
        # models.pyのUserから、対象ユーザー取得
        user = User.query.filter_by(username=username).first()   #最初に見つけたusernameをuserに入れる
        # 認証判定
        if user is not None and user.check_password(password):
            # 成功
            # 引数として渡されたuserオブジェクトを使用して、ユーザーをログイン状態にする
            login_user(user)
            # 画面遷移
            return redirect(url_for("top"))
        # 失敗
        flash("認証不備です")

    # GET
    return render_template('forms/login.html', form=loginform)    #ログイン画面へ


# ログアウト
@auth_bp.route("/logout")
@login_required     
def logout():
    # 現在ログインしているユーザーをログアウトする
    logout_user()
    # フラッシュメッセージ
    flash("ログアウトしました")   
    # 画面遷移
    return redirect(url_for("auth.login"))


# 新規登録
@auth_bp.route('/forms/register', methods=['GET', 'POST'])
def touroku():
    registerform = RegisterForm()     #forms.pyのRegisterFormクラスからオブジェクトを作る
    # POST
    if registerform.validate_on_submit():   
        session['name'] = registerform.name.data           #セッションとして保存。登録完了ページで使う。
        session['password'] = registerform.password.data     
         # データ入力取得
        username = registerform.name.data
        password = registerform.password.data
        # モデルを生成
        user = User(username=username)
        # パスワードハッシュ化
        user.set_password(password)
        # 登録処理
        db.session.add(user)
        db.session.commit()
        
        # 画面遷移 
        return redirect(url_for('auth.tourokuOK'))   
    
    # GET
    return render_template('forms/touroku.html', form=registerform)

# 登録完了
@auth_bp.route('/tourokuOK')
def tourokuOK():
    return render_template('forms/tourokuOK.html')