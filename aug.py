from flask import Flask,render_template,request,session
import base
import time
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
secret_key = os.environ.get("FLASK_SECRET_KEY")
if not secret_key:
    raise ValueError("CRITICAL ERROR: FLASK_SECRET_KEY is not set in the environment or .env file!")
app.secret_key=secret_key
text_input=""
Page=""
start=0
@app.route("/",methods=['POST','GET'])
def home():
    show_top_layer=True
    if request.method=='POST' and 'remove_layer' in request.form:
        show_top_layer=False
        session["start"]=int(time.perf_counter())
    return render_template("firstpage.html",show_top_layer=show_top_layer)  

@app.route("/submit",methods=['POST','GET'])
def submit():
    end=int(time.perf_counter())
    start=session.get("start")
    text_input=request.form.get('user_input')+" "
    base.recheck(text_input)
    diff=int(end-start)
    wpm=base.words//(diff/60)
    accuracy=base.q
    return render_template("secondpage.html",Page=wpm,Newpg=accuracy)
if __name__=="__main__":
    app.run(debug=True,port=8080)
