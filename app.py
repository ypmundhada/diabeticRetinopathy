from flask import Flask,request, url_for, redirect, render_template
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("DR_model.pkl", "rb"))
scaler = pickle.load(open("ST_scaler.pkl", "rb"))

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    text1 = request.form['1']
    text2 = request.form['2']
    text3 = request.form['3']
    text4 = request.form['4']
    text5 = request.form['5']
    text6 = request.form['6']
    text7 = request.form['7']
    text8 = request.form['8']
 
    row_df = pd.DataFrame([pd.Series([text1,text2,text3,text4,text5,text6,text7,text8])])
    sc_row_df = scaler.transform(row_df)
    print(row_df)
    prediction=model.predict(sc_row_df)
    output = prediction[0]
    if output==1:
        return render_template('result.html',pred='You have chance of having diabetes')
    else:
        return render_template('result.html',pred='You are safe. as your chance of prediction is low')




if __name__ == '__main__':
    app.run()
