# Flaskアプリケーションとデータベースの動作に関する設定
class Config(object):
    # CSRFやセッションで使用
    SECRET_KEY = "z2PMiQVn"       #推測されにくいランダムな文字列
    # 警告対策
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DB設定
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.sqlite"
