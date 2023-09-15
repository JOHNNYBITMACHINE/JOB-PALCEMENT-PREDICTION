from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
from sklearn import *

model = pickle.load(open("appPkl.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method=='GET':
        return render_template("home.html")
    else:
        gender = str(request.form['gender'])
        ssc_percentage= float(request.form['ssc_percentage'])
        ssc_board = str(request.form['ssc_board'])
        hsc_percentage = float(request.form['hsc_percentage'])
        hsc_board = str(request.form['hsc_board'])
        hsc_subject = str(request.form['hsc_subject'])
        degree_percentage= float(request.form['degree_percentage'])
        undergrad_degree = str(request.form['undergrad_degree'])
        work_experience = str(request.form['work_experience'])
        emp_test_percentage = float(request.form['emp_test_percentage'])
        specialisation = str(request.form['specialisation'])
        mba_percent = float(request.form['mba_percent'])
        input_data = np.array([[gender,ssc_percentage, ssc_board, hsc_percentage, hsc_board, hsc_subject, degree_percentage, undergrad_degree, work_experience, emp_test_percentage, specialisation, mba_percent]])
        result = model.predict(input_data)
        return render_template("home.html", 
                               result = result, 
                               gender= gender, 
                               ssc_percentage= ssc_percentage,
                               hsc_percentage= hsc_percentage,
                                hsc_board= hsc_board,
                                hsc_subject= hsc_subject,
                               degree_percentage= degree_percentage,
                                undergrad_degree= undergrad_degree,
                                work_experience= work_experience,
                                emp_test_percentage= emp_test_percentage, 
                               specialisation= specialisation,
                                mba_percent= mba_percent
                               )
    

        





if __name__ == "__main__":
    app.run(debug=True)















