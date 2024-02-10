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
    loginform = LoginForm()      #forms.pyのLoginFormクラスからオブジェクトを作る
    # POST
    if loginform.validate_on_submit():    #validatorsが表示されないなら、  
        return redirect(url_for('top'))     #リダイレクトでユーザー名、パスワードの二重送信を防ぐ。
    # GET
    return render_template('forms/login.html', form=loginform)    #ログイン画面へ

# 新規登録
@app.route('/forms/register', methods=['GET', 'POST'])
def touroku():
    registerform = RegisterForm()     #forms.pyのRegisterFormクラスからオブジェクトを作る
    # POST
    if registerform.validate_on_submit():   
        session['name'] = registerform.name.data           #セッションとして保存。登録完了ページで使う。
        session['password'] = registerform.password.data     
        
        return redirect(url_for('tourokuOK'))   
    
    # GET
    return render_template('forms/touroku.html', form=registerform)

# 登録完了
@app.route('/tourokuOK')
def tourokuOK():
    return render_template('forms/tourokuOK.html')


@app.route('/top')
def top():
    return render_template('top.html')    


@app.route('/puzzle') 
def puzzle():
    return render_template('game/15puzzle.html')

@app.route('/Shooting') 
def Shooting():
    return render_template('game/Shooting.html')

@app.route('/Cards') 
def Cards():
    return render_template('game/FlipCards.html')

@app.route('/reversi') 
def Reversi():
    return render_template('game/ReversiblePiece.html')

@app.route('/Dungeon') 
def Dungeon():
    return render_template('game/Dungeon.html')


@app.route('/FunkyBlocks') 
def FunkyBlocks():
    return render_template('game/FunkyBlocks.html')


  
@app.route('/Jumper') 
def Jumper():
    return render_template('game/Jumper.html')

@app.route('/CarryIt') 
def CarryIt():
    return render_template('game/CarryIt.html')

  

@app.route('/saturnvoyager') 
def saturnvoyager():
    return render_template('game/saturnvoyager.html')

@app.route('/EggCatch') 
def EggCatch():
    return render_template('game/EggCatch.html')


@app.route('/chase') 
def chase():
    return render_template('game/Chase.html')

@app.route('/Billiard') 
def Billiard():
    return render_template('game/Billiard.html')

@app.route('/yasai') 
def yasai():
    return render_template('game/yasai.html')

if __name__ == '__main__':
    app.run()