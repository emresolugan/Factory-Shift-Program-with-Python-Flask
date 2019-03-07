
# model dosyası burada veritabanına bağlantı ve query kısımlarını hallediyoruz.

from flask import render_template
from flask import request
import pypyodbc
connection = pypyodbc.connect(driver='{SQL Server Native Client 11.0}', server='localhost', database='Vardiya',
               trusted_connection='yes')

def get_operation():
    operationcursor = connection.cursor()
    operationcursor.execute(
        "SELECT Operation.Operation, Machine.MachineName, Operator.OperatorName, Shift.DateInterval, Hours.HoursInterval FROM Operation INNER JOIN Machine ON Operation.MachineID = Machine.MachineID INNER JOIN Operator ON Operation.OperatorID = Operator.OperatorID INNER JOIN Shift ON Operation.ShiftID = Shift.ShiftID INNER JOIN ShiftHour ON ShiftHour.ShiftID = Operation.ShiftID and ShiftHour.OperatorID = Operator.OperatorID INNER JOIN Hours ON Hours.ID = ShiftHour.HoursID;")
    oresult = operationcursor.fetchall()
    print(oresult)
    return oresult

def get_shift():
     shiftcursor = connection.cursor()
     shiftcursor.execute("SELECT ShiftDesc, DateInterval, ShiftTempo.TempoDescription, Hours.HoursInterval FROM Shift INNER JOIN ShiftHour ON Shift.ShiftID = ShiftHour.ShiftID INNER JOIN Hours ON ShiftHour.HoursID = Hours.ID INNER JOIN ShiftTempo ON Shift.Tempo = ShiftTempo.TempoID;")
     sresult = shiftcursor.fetchall()
     print(sresult)
     return sresult

def get_hours():
    hourscursor = connection.cursor()
    hourscursor.execute("SELECT * FROM  Hours")
    hours = hourscursor.fetchall()
    print(hours)
    return hours

def get_tempo():
    tempocursor = connection.cursor()
    tempocursor.execute("SELECT * FROM  ShiftTempo")
    tempo = tempocursor.fetchall()
    print(tempo)
    return tempo

def add_shift():
    if request.form:
        if request.form.get("vhour3") == "" and (request.form.get("vhour2") == ""):   # Eğer ikinci ve üçüncü vardiya saati girilmediyse
            shiftcursor = connection.cursor()
            shifthourcursor = connection.cursor()
            insert_shift = ("Insert into Shift (ShiftDesc, Tempo, DateInterval) values(?,?,?)")
            Values = [request.form.get("vname"), int(request.form.get("vtempo")), request.form.get("vdate")]
            shiftcursor.execute(insert_shift, Values)
            connection.commit()
            #------- Bu kısma kadar vardiyayı ekledik ------
            shiftcursor.execute("select ShiftID from Shift where ShiftID=(select max(ShiftID) from Shift)")
            shift_ID = shiftcursor.fetchall()
            print(shift_ID[0][0])
            print(request.form.get("vhour"))
            insert_hours = ("Insert into ShiftHour (ShiftID, HoursID) values(?,?)")
            Values2 = [shift_ID[0][0], int(request.form.get("vhour"))]
            shiftcursor.execute(insert_hours, Values2)
            connection.commit()
            #--------  En son vardiya saat tablosuna da ilişkiyi ekledik

        elif (request.form.get("vhour3") == "") and ((request.form.get("vhour2") != "")): # Eğer 3. vardiya saati girilmeyip sadece ikinci girildiyse
            shiftcursor = connection.cursor()
            shifthourcursor = connection.cursor()
            insert_shift = ("Insert into Shift (ShiftDesc, Tempo, DateInterval) values(?,?,?)")
            Values = [request.form.get("vname"), int(request.form.get("vtempo")), request.form.get("vdate")]
            shiftcursor.execute(insert_shift, Values)
            connection.commit()
            #------- Bu kısma kadar vardiyayı ekledik ------
            shiftcursor.execute("select ShiftID from Shift where ShiftID=(select max(ShiftID) from Shift)")
            shift_ID = shiftcursor.fetchall()
            print(shift_ID[0][0])
            print(request.form.get("vhour"))
            insert_hours = ("Insert into ShiftHour (ShiftID, HoursID) values(?,?)")
            Values2 = [shift_ID[0][0], int(request.form.get("vhour"))]
            Values3 = [shift_ID[0][0], int(request.form.get("vhour2"))]
            shiftcursor.execute(insert_hours, Values2)
            shiftcursor.execute(insert_hours, Values3)
            connection.commit()
            #--------  En son vardiya saat tablosuna da ilişkiyi ekledik
        elif (request.form.get("vhour3") != ""): # Eğer hepsi girilmişse
            shiftcursor = connection.cursor()
            shifthourcursor = connection.cursor()
            insert_shift = ("Insert into Shift (ShiftDesc, Tempo, DateInterval) values(?,?,?)")
            Values = [request.form.get("vname"), int(request.form.get("vtempo")), request.form.get("vdate")]
            shiftcursor.execute(insert_shift, Values)
            connection.commit()
            #------- Bu kısma kadar vardiyayı ekledik ------
            shiftcursor.execute("select ShiftID from Shift where ShiftID=(select max(ShiftID) from Shift)")
            shift_ID = shiftcursor.fetchall()
            print(shift_ID[0][0])
            print(request.form.get("vhour2"))
            insert_hours = ("Insert into ShiftHour (ShiftID, HoursID) values(?,?)")
            Values2 = [shift_ID[0][0], int(request.form.get("vhour"))]
            Values3 = [shift_ID[0][0], int(request.form.get("vhour2"))]
            Values4 = [shift_ID[0][0], int(request.form.get("vhour3"))]
            shiftcursor.execute(insert_hours, Values2)
            shiftcursor.execute(insert_hours, Values3)
            shiftcursor.execute(insert_hours, Values4)
            connection.commit()
            #--------  En son vardiya saat tablosuna da ilişkiyi ekledik
        return 1
    else:
        return 2

def get_machines():
    machinecursor = connection.cursor()
    machinecursor.execute("SELECT * FROM  Machine")
    machines = machinecursor.fetchall()
    print(machines)
    return machines

def get_operators():
    operatorcursor = connection.cursor()
    operatorcursor.execute("SELECT * FROM  Operator")
    operators = operatorcursor.fetchall()
    print(operators)
    return operators

def get_all_shifts():
    shiftcursor = connection.cursor()
    shiftcursor.execute("SELECT * FROM  Shift")
    shifts = shiftcursor.fetchall()
    print(shifts)
    return shifts

def get_shift_hours():
    shiftcursor = connection.cursor()
    shiftcursor.execute("SELECT * FROM  ShiftHour")
    shifthours = shiftcursor.fetchall()
    print(shifthours)
    return shifthours

def get_experiences():
    experiencecursor = connection.cursor()
    experiencecursor.execute("SELECT * FROM  OperatorMachineExperience")
    experiences = experiencecursor.fetchall()
    print(experiences)
    return experiences

def add_operation():
    operatorcursor = connection.cursor()
    operatorcursor.execute("SELECT * FROM  Operator WHERE OperatorID = " + request.form.get("ooperator"))
    operator = operatorcursor.fetchall()

    machinecursor = connection.cursor()
    machinecursor.execute("SELECT *  FROM Machine WHERE MachineID = " + request.form.get("omachine"))
    machine = machinecursor.fetchall()

    if request.form:

        if (machine[0][2] != 5):  # Eğer makine durumu kullanılabilir değilse
            return "machine_alert"

        elif ((operator[0][4] == 3) or (operator[0][4] == 5) or (operator[0][4] == 7) and (int(request.form.get("oshifthour")) == 3 or int(request.form.get("oshifthour")) == 5 or int(request.form.get("oshifthour")) == 7)):  # Eğer operatörün bir önceki vardiyası gece ise
            return "operator_night_alert"

        else:
            operationcursor = connection.cursor()
            operatorcursor = connection.cursor()
            hourcursor = connection.cursor()
            insert_operation = ("Insert into Operation (Operation, MachineID, OperatorID, ShiftID) values(?,?,?,?)")
            Values = [request.form.get("oname"), int(request.form.get("omachine")), request.form.get("ooperator"), request.form.get("oshift")]
            operationcursor.execute(insert_operation, Values)
            connection.commit()
            # ------- Bu kısma kadar operasyonu ekledik ------
            operatorcursor.execute("Update Operator Set LastShiftHour = '%s' Where OperatorID = '%s'" % (request.form.get("oshifthour"), request.form.get("ooperator")))
            connection.commit()
            # ------- Bu kısımda operatörün son çalışma saatini güncelliyoruz ------
            hourcursor.execute("Update ShiftHour Set OperatorID = '%s' Where HoursID = '%s' And ShiftID = '%s'" % (request.form.get("ooperator"), request.form.get("oshifthour"), request.form.get("oshift")))
            connection.commit()
            return 1

    else:
        return 2