from flask import Blueprint, render_template, request, flash, redirect
from datetime import datetime, date, time, timedelta
from flask_security import login_required
from user_page.forms import ServiceForm
from user_page.models import Service
from app import db
from flask_security.core import current_user


user_page = Blueprint('user_page', __name__, template_folder='templates')


@user_page.route('/', methods=['GET'])
@login_required
def test():
    my_datetime = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)#.isoformat(' ', timespec='minutes')
    list_calender_finish = []
    list_calendar = []
    for i in range(1, 40):
        list_calendar.append(my_datetime)
        for y in range(1, 48):
            my_datetime += timedelta(minutes=30)
            list_calendar.append(my_datetime)
        list_calender_finish.append(list_calendar)
        list_calendar = []
        my_datetime += timedelta(minutes=30)
    time_start = time(hour=10)
    time_finsh = time(hour=18)
    print(list_calender_finish)
    return render_template('user_page/user_page.html', list_calender_finish=list_calender_finish, time_start=time_start,
                           time_finsh=time_finsh)


@user_page.route('/service', methods=['GET'])
@login_required
def service():
    services = Service.query.all()
    return render_template('user_page/service.html', services=services)


@user_page.route('/add_service', methods=['GET', 'POST'])
@login_required
def add_service():
    form = ServiceForm(request.form)
    if request.method == 'POST' and form.validate():
        service = Service(
                    name_service = form.name_service.data,
                    service_time = form.service_time.data,
                    prise_service = form.prise_service.data)
        db.session.add(service)
        db.session.commit()
        flash('Thanks for registering')
        print("yes")#return redirect('service')
        #return redirect(url_for('security.login'))
    return render_template('user_page/add_service.html', form=form)