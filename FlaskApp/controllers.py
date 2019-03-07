
# controller dosyası burada sayfanın get ve post metodları bulunuyor ayrıca model ve view ile bir köprü kuruluyor.

from flask import render_template
from flask import request
import models

# GET
def get_operation():
    oresult = models.get_operation()
    return render_template("operation_calendar.html", oresult=oresult)

# GET
def get_shift():
    sresult = models.get_shift()
    return render_template("shift_calendar.html", sresult=sresult)

# GET
def get_addshift():
    hours = models.get_hours()
    tempo = models.get_tempo()
    return render_template("add_shift.html", hours=hours, tempo=tempo)

# POST
def post_addshift():
    if models.add_shift() == 1:
        sresult = models.get_shift()
        return render_template("shift_calendar.html", sresult=sresult)
    elif models.add_shift() == 2:
        return render_template("404")

# GET
def get_addoperation():
    machines = models.get_machines()
    operators = models.get_operators()
    shifts = models.get_all_shifts()
    shifthours = models.get_shift_hours()
    hours = models.get_hours()
    experiences = models.get_experiences()
    return render_template("add_operation.html", machines=machines, operators=operators, shifts=shifts, shifthours=shifthours, hours=hours, experiences=experiences, alertt=0)

# POST
def post_addoperation():

    return_value = models.add_operation()

    if return_value == "machine_alert":
        machines = models.get_machines()
        operators = models.get_operators()
        shifts = models.get_all_shifts()
        shifthours = models.get_shift_hours()
        hours = models.get_hours()
        experiences = models.get_experiences()
        return render_template("add_operation.html", machines=machines, operators=operators, shifts=shifts, shifthours=shifthours, hours=hours, experiences=experiences, alertt=1)

    elif return_value == "operator_night_alert":

        machines = models.get_machines()
        operators = models.get_operators()
        shifts = models.get_all_shifts()
        shifthours = models.get_shift_hours()
        hours = models.get_hours()
        experiences = models.get_experiences()
        return render_template("add_operation.html", machines=machines, operators=operators, shifts=shifts,
                               shifthours=shifthours, hours=hours, experiences=experiences, alertt=2)


    elif return_value == 1:
        oresult = models.get_operation()
        return render_template("operation_calendar.html", oresult=oresult)

    elif return_value == 2:
        return render_template("404")

