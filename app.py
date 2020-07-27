from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore, Security, current_user

from flask import redirect, url_for, request
from flask_admin import AdminIndexView


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


from models import User, Role
from user_page.models import Service

class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Role, db.session))
admin.add_view(AdminView(Service, db.session))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)