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
    if request.form["WW1"] == "1914":
        session["Q1"] = True
    else:
        session[Q1] = False
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["first_name"] = request.form["firstName"]
    session["last_name"] = request.form["lastName"]
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["favorite_color"] = request.form["favoriteColor"]
    return render_template('page3.html')
    
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    session["favorite_color"] = request.form["favoriteColor"]
    return render_template('page4.html')
  
@app.route('/page5',methods=['GET','POST'])
def renderPage5():
    session["favorite_color"] = request.form["favoriteColor"]
    return render_template('page4.html')
    
@app.route('/end',methods=['GET','POST'])
def renderFinalPage():
    #TODO: save the favorite color in the session
    session["favorite_color"] = request.form["favoriteColor"]
    return render_template('final_page.html')
    
    
if __name__=="__main__":
    app.run(debug=False)
