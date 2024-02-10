from flask_wtf import FlaskForm                   
from wtforms import StringField, EmailField, SubmitField, PasswordField     
from wtforms.validators import DataRequired, Email, Length, EqualTo    #バリデーターを使うためインポート

#pip install flask-wtf==1.1.1 

# ==================================================
# Formクラス
# ==================================================
# ログイン画面    
class LoginForm(FlaskForm):
    name = StringField('名前：', validators=[DataRequired('必須入力です')])
    password = PasswordField('パスワード：', validators=[Length(3, 10, 'パスワードの長さは3文字以上10文字以内です')])
    
    submit = SubmitField('ログイン')

# 新規登録画面
class RegisterForm(LoginForm):   #ログイン画面のLoginFormクラスを継承する
    confirm_password = PasswordField('パスワード確認：', validators=[EqualTo('password', "パスワードが一致しません")])
    
    submit = SubmitField('送信')   #送信ボタン  オーバーライドしてる

