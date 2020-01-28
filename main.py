from app import app
from app import db
from user_page.blueprint import user_page
import view


app.register_blueprint(user_page, url_prefix='/user_page')


if __name__ == '__main__':
    app.run()