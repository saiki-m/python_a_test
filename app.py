import os    # 乱数を設定するためインポート
from flask import Flask, render_template, session, redirect, url_for
from forms import LoginForm, RegisterForm

app = Flask(__name__)


# 乱数を設定
app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/")
def hello():
    return render_template("index.html")

#ログイン
@app.route('/forms/login', methods=['GET', 'POST'])
def login():
    form2 = LoginForm()      #ファイルforms.pyのLoginFormクラスからオブジェクトを作る
    # POST
    if form2.validate_on_submit():    #validatorsの内容が表示されないなら、  
        return redirect(url_for('top'))     #redirectとすることで、ユーザー名、パスワードの二重送信を防ぐ。
    # GETリクエストで、ifが通らなかった場合。form2オブジェクトを引数としてformにわたす。
    return render_template('forms/login.html', form=form2)    #ログイン画面へ

# 登録
@app.route('/forms/touroku', methods=['GET', 'POST'])
def touroku():
    form = RegisterForm()     #ファイルforms.pyのRegisterFormクラスからオブジェクトを作る
        #ファイルforms.pyのRegisterFormクラスからオブジェクトを作る
    # POST
    if form.validate_on_submit():    #validatorsの内容が表示されないなら、
        session['name'] = form.name.data           #セッションとして保存。登録完了ページで使う。
        session['password'] = form.password.data     
        
        return redirect(url_for('tourokuOK'))   #redirectとすることで、ユーザー名、パスワードの二重送信を防ぐ。PRGパターンのR。
    
    # GETリクエストで、ifが通らなかった場合。formオブジェクトを引数としてformにわたす。
    return render_template('forms/touroku.html', form=form)

# 登録完了画面
@app.route('/tourokuOK')
def tourokuOK():
    return render_template('forms/tourokuOK.html')


@app.route('/top')
def top():
    return render_template('top.html')    





@app.route('/puzzle') 
def puzzle():
    return render_template('login/templates/game/15puzzle.html')

@app.route('/Shooting') 
def Shooting():
    return render_template('login/templates/game/Shooting.html')

@app.route('/Cards') 
def Cards():
    return render_template('login/templates/game/FlipCards.html')

@app.route('/reversi') 
def Reversi():
    return render_template('login/templates/game/ReversiblePiece.html')

@app.route('/Dungeon') 
def Dungeon():
    return render_template('login/templates/game/Dungeon.html')


@app.route('/FunkyBlocks') 
def FunkyBlocks():
    return render_template('login/templates/game/FunkyBlocks.html')


  
@app.route('/Jumper') 
def Jumper():
    return render_template('login/templates/game/Jumper.html')

@app.route('/CarryIt') 
def CarryIt():
    return render_template('login/templates/game/CarryIt.html')

  

@app.route('/saturnvoyager') 
def saturnvoyager():
    return render_template('login/templates/game/saturnvoyager.html')

@app.route('/EggCatch') 
def EggCatch():
    return render_template('login/templates/game/EggCatch.html')


@app.route('/chase') 
def chase():
    return render_template('login/templates/game/Chase.html')

@app.route('/Billiard') 
def Billiard():
    return render_template('login/templates/game/Billiard.html')

@app.route('/yasai') 
def yasai():
    return render_template('login/templates/game/yasai.html')

if __name__ == '__main__':
    app.run()