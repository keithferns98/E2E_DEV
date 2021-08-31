import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from flask import Flask,request,render_template
import pickle

app=Flask(__name__)
q=""
@app.route("/")
def loadPage():
    return render_template('home.html',query='')

@app.route('/',methods=['POST'])
def cancerPredict():

    #5 input queries from the user post method allows us
    input1=request.form['query1']
    input2=request.form['query2']
    input3=request.form['query3']
    input4=request.form['query4']
    input5=request.form['query5']
    data=[[input1,input2,input3,input4,input5]]
    new_df=pd.DataFrame(data,columns=['texture_mean','perimeter_mean','smoothness_mean','compactness_mean','symmetry_mean'])

    model = pickle.load(open("model.sav", "rb"))
    y_pred=model.predict(new_df)
    probability=model.predict_proba(new_df)[:,1]
    if y_pred==1:
        o1="The patient is diagnosed with Breast Cancer"
        o2="Confidence {}".format(probability*100)
    else:
        o1="The patient is healthy and not diagnosed with Breast Cancer"
        o2="Confidence {} ".format(probability*100)
    return render_template('home.html',output1=o1,output2=o2,query1=request.form['query1'],query2=request.form['query2'],query3=request.form['query3'],query4=request.form['query4'],query5=request.form['query5'])
app.run()