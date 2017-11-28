from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import db.connect as connection
from flask_wtf import Form
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/hospital'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
CSRFProtect(app)

cnt = connection.connection()

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    class AddPatient(Form):
        patientid = StringField()
        pfname = StringField()
        plname = StringField()
        page = StringField()
        pgender = StringField()
        paddress = StringField()

    form = AddPatient()

    if request.method == 'POST':
        cnt.post_patient(form.patientid.data, form.pfname.data, form.plname.data, form.page.data, form.pgender.data, form.paddress.data)
        return redirect('/patients')

    return render_template('/add_patient.html', form=form)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visits')
def visits():
    visits = cnt.get_visits()
    return render_template('/visits.html', columns=visits)

@app.route('/patients', methods=['GET', 'POST'])
def patients():
    patients = cnt.get_patients()
    return render_template("/patients.html", columns=patients)

@app.route('/employees')
def employees():
    employees = cnt.get_employees()
    return render_template('/employees.html', columns=employees)

@app.route('/views')
def views():
    views = cnt.get_views()
    views2 = cnt.get_views2()
    views3 = cnt.get_views3()
    views4 = cnt.get_views4()
    views5 = cnt.get_views5()
    views6 = cnt.get_views6()
    views7 = cnt.get_views7()
    views8 = cnt.get_views8()
    views9 = cnt.get_views9()
    return render_template('/views.html', columns=views, columns2=views2, columns3=views3, columns4=views4, columns5=views5, columns6=views6, columns7=views7, columns8=views8, columns9=views9)


if __name__ == '__main__':
    app.run()