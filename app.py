# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request
import numpy as np
import pickle


app = Flask(__name__)
model=pickle.load(open('kidisRanF.pkl','rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])

def predict ():
    if request.method == 'POST':
        sg = float(request.form['sg'])
        htn = float(request.form['htn'])
        dm = float(request.form['dm'])
        hemo =float(request.form['hemo'])
        al = float(request.form['al'])
        appet = float(request.form['appet'])
        pe = float(request.form['pe'])
        pc = float(request.form['pc'])
        
        
        values = np.array([[sg,htn,dm,hemo,al,appet,pe,pc]])
        prediction = model.predict(values)
        
        return render_template('result.html', prediction=prediction)

if __name__=='__main__':
    app.run(debug=True)
    