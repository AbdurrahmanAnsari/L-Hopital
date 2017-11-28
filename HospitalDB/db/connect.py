import psycopg2

class connection():
    def __init__(self):
        con = psycopg2.connect(database='hospitaldb', user='postgres', host='localhost', password='root')
        self.cur = con.cursor()

    def get_patients(self):
        self.cur.execute('SELECT * FROM patients')
        return self.cur.fetchall()

    def post_patient(self, patient_id, fname, lname, age, gender, address):
        self.cur.execute('INSERT INTO patients VALUES (%d, %s, %s, %d, %s, %s)', (patient_id, fname, lname, age, gender, address))
        return self.get_patients()

    def get_employees(self):
        self.cur.execute('SELECT * FROM employees')
        return self.cur.fetchall()

    def get_visits(self):
        self.cur.execute('SELECT * FROM visits')
        return self.cur.fetchall()

    def get_departments(self):
        self.cur.execute('SELECT "Department_ID" FROM departments')
        return self.cur.fetchall()

    def get_views(self):
        self.cur.execute('SELECT "P_F_Name", "P_L_Name", "E_F_Name", "E_L_Name" FROM patients, employees, visits WHERE "V_Patient_ID"="Patient_ID" AND "V_Doctor_ID"="Employee_ID"')
        return self.cur.fetchall()

    def get_views2(self):
        self.cur.execute('SELECT "Employee_ID", "E_F_Name", "E_L_Name" FROM employees WHERE "E_Age" = ANY(SELECT "E_Age" FROM employees WHERE "E_Age" >=60)')
        return self.cur.fetchall()

    def get_views3(self):
        self.cur.execute('SELECT "E_F_Name", "E_L_Name" FROM employees WHERE "Employee_ID" = (SELECT "V_Doctor_ID" FROM visits WHERE "V_Patient_ID" = (SELECT "Patient_ID" FROM patients WHERE "P_F_Name" = \'Nicholas\' AND "P_L_Name" = \'Ward\'))')
        return self.cur.fetchall()

    def get_views4(self):
        self.cur.execute('SELECT "Employee_ID", "E_F_Name", "E_L_Name" FROM employees FULL OUTER JOIN patients ON ("E_F_Name" = "P_F_Name" AND "E_L_Name" = "P_L_Name" AND "E_Address" = "P_Address")')
        return self.cur.fetchall()

    def get_views5(self):
        self.cur.execute('SELECT COUNT("Employee_ID") FROM employees')
        return self.cur.fetchall()

    def get_views6(self):
        self.cur.execute('SELECT COUNT("Room_Number") FROM rooms')
        return self.cur.fetchall()

    def get_views7(self):
        self.cur.execute('SELECT COUNT("Patient_ID") FROM patients WHERE "P_Address" LIKE \'%Drive\'')
        return self.cur.fetchall()

    def get_views8(self):
        self.cur.execute('SELECT "Department_Name" FROM departments WHERE (SELECT COUNT("Employee_ID") FROM employees) < 50000')
        return self.cur.fetchall()

    def get_views9(self):
        self.cur.execute('SELECT "Prescription" FROM visits WHERE "V_Patient_ID" = (SELECT "Patient_ID" FROM patients WHERE "P_F_Name" = \'Raymond\' AND "P_L_Name" = \'Bell\')')
        return self.cur.fetchall()
