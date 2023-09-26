from flask import Blueprint

news_bp = Blueprint('news', __name__, template_folder='news_templates')
from news import news_views
