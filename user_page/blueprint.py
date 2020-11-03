from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime, date, time, timedelta
from flask_security import login_required
from user_page.forms import ServiceForm
from user_page.models import Service
from app import db
from flask_security.core import current_user


user_page = Blueprint('user_page', __name__, template_folder='templates')

@user_page.route('/<login>', methods=['GET'])
@login_required
def test(login):
    print(login)
    if current_user.login == login:
        my_datetime = datetime(2020, 5, 13, 0, 0, 0, 0)
        my_time = time(0, 0)
        print(my_time)
        if not my_datetime:
            my_datetime = datetime.today().replace( hour=0, minute=0, second=0, microsecond=0)#.isoformat(' ', timespec='minutes')
        my_datetime = my_datetime - timedelta(days = int(my_datetime.weekday()))
        weeks = []
        week = []
        day_dict = {}
        for i in range(5):
            weeks.append(my_datetime)
            my_datetime += timedelta(days=7)
        return render_template("user_page/user_page.html", weeks=weeks, date=date, time=time)
    return redirect(url_for('security.login'))


@user_page.route('/beta/<week>')
@login_required
def test_beta(week):
    my_datetime = datetime.fromisoformat(week)
    day_dict={}
    week = []
    services = {datetime(2020, 5, 13, 13, 0, 0, 0): {"master":"{}".format(current_user.login),
                                                     "time": 30,
                                                     "time_work": datetime(2020, 5, 13, 13, 0, 0, 0)+timedelta(
                                                         minutes=30),
                                                     "name": "Танюха"},
                datetime(2020, 5, 13, 18, 0, 0, 0): {"master": "{}".format(current_user.login),
                                                     "time": 30,
                                                     "time_work": datetime(2020, 5, 13, 18, 0, 0, 0) + timedelta(
                                                         minutes=30),
                                                     "name": "olesia"}
                }
    for y in range(7):
        keys_for_data = my_datetime
        day_dict[keys_for_data] = {}
        day_dict[keys_for_data][my_datetime] = None
        for x in range(47):
            my_datetime += timedelta(minutes=30)
            if my_datetime in services:
                service = {}
                service[my_datetime] = services.pop(my_datetime)
                day_dict[keys_for_data][my_datetime] = service
                my_datetime = service[my_datetime]["time_work"] - timedelta(minutes=30)
            else:
                day_dict[keys_for_data][my_datetime] = None
        my_datetime += timedelta(minutes=30)
    week.append(day_dict)
    day_dict = {}
    time_start = time(hour=10)
    time_finsh = time(hour=20)
    return render_template("user_page/calendar_week.html", week=week,  time_start=time_start, time_finsh=time_finsh)

@user_page.route('/<my_time>')
@login_required
def test_beta_2(my_time):
    return render_template('user_page/beta_add.html')

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
        return redirect('service')
        #return redirect(url_for('security.login'))
    return render_template('user_page/add_service.html', form=form)