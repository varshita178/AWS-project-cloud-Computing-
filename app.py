
from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file

app = Flask(__name__)

import Database as db

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/insert',methods = ['POST'])
def insert():
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        phone = request.form['phone']
        rating = request.form['grade']
        comment = request.form['comment']
        db.insert_details(name,age,email,phone,rating,comment)
        details = db.get_details()
        print(details)
        for d in details:
            var=d
        return render_template('index.html',details=details,var=var)



if __name__ == "__main__":
    
    app.run(host="0.0.0.0",port="80")