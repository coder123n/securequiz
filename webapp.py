import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #SECRET_KEY is an environment variable.  
                                         #The value should be set in Heroku (Settings->Config Vars).  

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear
    return redirect('/')

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if "Q1" not in session:
        session["Q1"] = request.form["WW1"]
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if "Q2" not in session:
        session["Q2"] = request.form["pres"]
    return render_template('page3.html')
    
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    if "Q3" not in session:
        session["Q3"] = request.form["titanic"]
    return render_template('page4.html')
  
@app.route('/page5',methods=['GET','POST'])
def renderPage5():
    if "Q4" not in session:
        session["Q4"] = request.form["WW2"]
    return render_template('page5.html')
    
@app.route('/end',methods=['GET','POST'])
def renderFinalPage():
    if "Q5" not in session:
        session["Q5"] = request.form["wonders"]
    percent = 0
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    if session["Q1"] == "1914":
        one = "You correctly answered " + session["Q1"] + " for Question 1."
        percent +=1
    else:
        one = "You answered " + session["Q1"] + " for Question 1. The correct answer was 1914"
    if session["Q2"] == "Abraham Lincoln":
        two = " You correctly answered " + session["Q2"] + " for Question 2."
        percent +=1
    else:
        two = " You answered " + session["Q2"] + " for Question 2. The correct answer was Abraham Lincoln"
    if session["Q3"] == "1912":
        three = " You correctly answered " + session["Q3"] + " for Question 3."
        percent +=1
    else:
        three = " You answered " + session["Q3"] + " for Question 3. The correct answer was 1912"
    if session["Q4"] == "1945":
        four = " You correctly answered " + session["Q4"] + " for Question 4."
        percent +=1
    else:
        four = " You answered " + session["Q4"] + " for Question 4. The correct answer was 1945"
    if session["Q5"] == "Great pyramid of Giza":
        five = " You correctly answered " + session["Q5"] + " for Question 5."
        percent +=1
    else:
        five = " You answered " + session["Q5"] + " for Question 5. The correct answer was the Great pyramid of Giza"
    percent = percent / 5
    percent = percent * 100
    return render_template('final_page.html',per=percent, one=one,two=two,three=three,four=four,five=five)
    
    
if __name__=="__main__":
    app.run(debug=True)
