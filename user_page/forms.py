from wtforms import Form, BooleanField, StringField, IntegerField, PasswordField, validators

class ServiceForm(Form):
    name_service = StringField('name_service', [validators.Length(min=3, max=25)])
    service_time = StringField('service_time', [validators.Length(min=1, max=35)])
    prise_service = IntegerField('prise_service')