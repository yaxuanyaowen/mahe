from flask import Flask
from users import users_bp
from news import news_bp

app = Flask(__name__)
app.secret_key = 'fdsgertsyh'

app.register_blueprint(users_bp, url_prefix='/login')
app.register_blueprint(news_bp, url_prefix='/news')

if __name__ == '__main__':
    app.run(debug=True)
