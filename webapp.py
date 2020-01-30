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
    session["Q1"] = request.form["WW1"]
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["Q2"] = request.form["pres"]
    return render_template('page3.html')
    
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    return render_template('page4.html')
  
@app.route('/page5',methods=['GET','POST'])
def renderPage5():
    return render_template('page5.html')
    
@app.route('/end',methods=['GET','POST'])
def renderFinalPage():
    percent = 0
    if session["Q1"] == "1914":
        percent = 1
    if session["Q2"] == "Abe":
        percent +=1
    if session["Q3"] == "1912":
        percent +=1
    if session["Q4"] == "1945":
        percent +=1
    if session["Q5"] == "Pyramid":
        percent +=1
    percent = percent / 5
    percent = percent * 100
    return render_template('final_page.html',per=percent)
    
    
if __name__=="__main__":
    app.run(debug=True)
