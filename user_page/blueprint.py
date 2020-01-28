from flask import Blueprint, render_template
from datetime import datetime
from flask_security import login_required

user_page = Blueprint('user_page', __name__, template_folder='templates')

@user_page.route('/', methods=['GET'])
@login_required
def my_def():
    return render_template('user_page/index.html')