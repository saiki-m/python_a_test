from flask import Flask, render_template, session, redirect, url_for, flash
from forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required,  LoginManager
from models import db, Memo, User
from flask_migrate import Migrate

app = Flask(__name__)

# config.py読み込み
app.config.from_object("config.Config")
# データベースとFlaskとの紐づけ
db.init_app(app)
# マイグレーションとの紐づけ（Flaskとdb）
migrate = Migrate(app, db)
# LoginManagerインスタンス
login_manager = LoginManager()
# LoginManagerとFlaskとの紐づけ
login_manager.init_app(app)
# ログインが必要なページにアクセスしようとしたときに表示されるメッセージを変更
login_manager.login_message = "認証していません：ログインしてください"
# 未認証のユーザーがアクセスしようとした際に
# リダイレクトされる関数名を設定する
login_manager.login_view = "login"

@login_manager.user_loader   #ユーザー情報を読み込む関数として「Flask-Login」に登録
def load_user(user_id):
    return User.query.get(int(user_id))    #user_idに対応するユーザー情報を取得


@app.route("/")
def hello():
    return render_template("index.html")

#ログイン
@app.route('/login/', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()      #forms.pyのLoginFormクラスからオブジェクトを作る
    # POST
    if loginform.validate_on_submit():    #validatorsが表示されないなら、  
        # データ入力取得
        username = loginform.name.data
        password = loginform.password.data
        # models.pyのUserから、対象ユーザー取得
        user = User.query.filter_by(username=username).first()
        # 認証判定
        if user is not None and user.check_password(password):
            # 成功
            # 引数として渡されたuserオブジェクトを使用して、ユーザーをログイン状態にする
            login_user(user)
            # 画面遷移
            return redirect(url_for("top"))

    # GET
    return render_template('forms/login.html', form=loginform)    #ログイン画面へ


# ログアウト
@app.route("/logout")
@login_required     
def logout():
    # 現在ログインしているユーザーをログアウトする
    logout_user()
    # フラッシュメッセージ
    flash("ログアウトしました")   
    # 画面遷移
    return redirect(url_for("login"))


# 新規登録
@app.route('/forms/register', methods=['GET', 'POST'])
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
        # フラッシュメッセージ
        flash("ユーザー登録しました")  
        # 画面遷移 
        return redirect(url_for('tourokuOK'))   
    
    # GET
    return render_template('forms/touroku.html', form=registerform)

# 登録完了
@app.route('/tourokuOK')
def tourokuOK():
    return render_template('forms/tourokuOK.html')


@app.route('/top')
@login_required
def top():
    return render_template('top.html')    


@app.route('/puzzle')
@login_required 
def puzzle():
    return render_template('game/15puzzle.html')

@app.route('/Shooting')
@login_required 
def Shooting():
    return render_template('game/Shooting.html')

@app.route('/Cards')
@login_required 
def Cards():
    return render_template('game/FlipCards.html')

@app.route('/reversi')
@login_required 
def Reversi():
    return render_template('game/ReversiblePiece.html')

@app.route('/Dungeon')
@login_required 
def Dungeon():
    return render_template('game/Dungeon.html')


@app.route('/FunkyBlocks')
@login_required 
def FunkyBlocks():
    return render_template('game/FunkyBlocks.html')


  
@app.route('/Jumper')
@login_required 
def Jumper():
    return render_template('game/Jumper.html')

@app.route('/CarryIt')
@login_required 
def CarryIt():
    return render_template('game/CarryIt.html')

  

@app.route('/saturnvoyager')
@login_required 
def saturnvoyager():
    return render_template('game/saturnvoyager.html')

@app.route('/EggCatch')
@login_required 
def EggCatch():
    return render_template('game/EggCatch.html')


@app.route('/chase')
@login_required 
def chase():
    return render_template('game/Chase.html')

@app.route('/Billiard')
@login_required 
def Billiard():
    return render_template('game/Billiard.html')

@app.route('/yasai')
@login_required 
def yasai():
    return render_template('game/yasai.html')

if __name__ == '__main__':
    app.run()