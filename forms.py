from flask_wtf import FlaskForm                   
from wtforms import StringField, EmailField, SubmitField, PasswordField     
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError   
from models import User

# ログイン画面    
class LoginForm(FlaskForm):
    name = StringField('名前：', validators=[DataRequired('必須入力です')])
    password = PasswordField('パスワード：', validators=[Length(3, 10, 'パスワードの長さは3文字以上10文字以内です')])
    
    submit = SubmitField('ログイン')
    
    # バリデータ作成
    # 英数字が含まれているかチェックする
    def validate_password(self, password):
        if not (any(c.isalpha() for c in password.data) and \
            any(c.isdigit() for c in password.data) ):     #c.isalphaはアルファベット、c.isdigitは数字
            raise ValidationError('パスワードには英数字を含める必要があります')



# 新規登録画面
class RegisterForm(LoginForm):   #継承
    confirm_password = PasswordField('パスワード確認：', validators=[EqualTo('password', "パスワードが一致しません")])
    
    submit = SubmitField('送信')   #オーバーライド

    # バリデータ作成
    def validate_name(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('そのユーザー名は既に使用されています')
