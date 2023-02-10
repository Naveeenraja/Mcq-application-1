from flask import Flask,render_template,request,redirect, url_for,session
from flask_session import Session
import datetime
from datetime import date, timedelta
import data.mcqutil as mcq_utils
import json 
file ="studreg.json"
file1 = "quiz.json"
file2= "quiz2.json"
file3= "quiz3.html"
file4= "quiz4.html"
app=Flask(__name__)
app.config["SECRET_KEY"]="somekey"
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

with open("quiz.json", "r") as file1:
    quiz_data1 = json.load(file1)

with open("quiz2.json", "r") as file2:
    quiz_data2 = json.load(file2)
    
with open("quiz3.json", "r") as file3:
    quiz_data3 = json.load(file3)    

with open("quiz4.json", "r") as file4:
    quiz_data4 = json.load(file4) 

def check_session():
    if len(session.keys())>0:
        return True
    else:
        return False

@app.route("/logout" , methods=["POST" , "GET"]) 
def logout():
    if check_session():
        session.pop("Email" , None)
        session.pop("Firstname" , None) 
    return redirect("/")      



@app.route("/", methods=["POST" , "GET"])
def index():
    return render_template("login.html")

@app.route("/tab/<page>", methods=["POST" , "GET"])
def about(page):
    if page=="about":
        return render_template("about.html")
    if page=="dashboard":
        return render_template("dashboard.html", email=session["Email"], fname=session["Firstname"], lname=session["Lastname"], dob=session["DOB"], gender=session["Gender"])
    if page=="mark":
        return render_template("mark.html", mark=session["Gk_Mark"],fname=session["Firstname"],per=session["Gk_Per"],time=session["Gk_Time_Taken"],date=session["Gk_date_exam"], mark1=session["chem_Mark"],fname1=session["Firstname"],per1=session["chem_Per"],time1=session["chem_Time_Taken"],date1=session["chem_date_exam"], mark2=session["Geo_Mark"],fname2=session["Firstname"],per2=session["Geo_Per"],time2=session["Geo_Time_Taken"],date2=session["Geo_date_exam"],mark3=session["Eng_Mark"],fname3=session["Firstname"],per3=session["Eng_Per"],time3=session["Eng_Time_Taken"],date3=session["Eng_date_exam"])
    if page=="about":
        return render_template("about.html")
    if page=="test":
        return render_template("test.html")
    if page=="help":
        return render_template("help.html" , fname=session["Firstname"])
    return redirect("/dashboard")
@app.route("/login", methods= ["POST","GET"])
def login():
    data = mcq_utils.read_json(file)
    return render_template("mcq.html",data=data["student registration"])

@app.route("/register", methods=["POST" , "GET"])
def reg():
   
    data = mcq_utils.read_json(file)
    if request.method=="POST":
        length=len(data["student registration"])
        fname=request.form["firstname"]
        lname=request.form["lastname"]
        date_of_birth= request.form["dob"]
        gender= request.form["inlineRadioOptions"]
        email= request.form["email"]
        username= request.form["username"]
        password= request.form["password"]
        list_of_stud={
            "s_no" : length+1,
            "Firstname" : fname,
            "Lastname"  : lname,
            "DOB" : date_of_birth,
            "Gender" : gender,
            "Email" : email,
            "Username" : username,
            "Password" : password,
            
            "Gk_Mark" : "",
            "Gk_Per" : "",
            "Gk_Time_Taken" : "",
            "Gk_date_exam": "",
            
            "chem_Mark" : "",
            "chem_Per" : "",
            "chem_Time_Taken" : "",
            "chem_date_exam": "",
            
            "Eng_Mark" : "",
            "Eng_Per" : "",
            "Eng_Time_Taken" : "",
            "Eng_date_exam": "",
            
            "Geo_Mark" : "",
            "Geo_Per" : "",
            "Geo_Time_Taken" : "",
            "Geo_date_exam": ""
        }
        data["student registration"].append(list_of_stud)
        mcq_utils.write_json(file,data)
        msg= username + " registration has been completed successfully !!"
        data = mcq_utils.read_json(file)
        return render_template("login.html",data=data["student registration"],msg=msg )
    return render_template("mcq2.html", data=data["student registration"])

@app.route("/dashboard", methods=["GET" , "POST"])
def dash():
    # if check_session():
        data = mcq_utils.read_json(file)
        message=""
        if request.method=="POST":                                                   
            email=request.form["Email"]
            password=request.form["Password"]
            message="incorrect password / email" 
            for i in data["student registration"] : 
                session["Firstname"]=i["Firstname"]
                session["Email"]=i["Email"]
                session["Lastname"]=i["Lastname"]
                session["DOB"]=i["DOB"]
                session["Gender"]=i["Gender"]
                session["Gk_Mark"]=i["Gk_Mark"]
                session["Gk_Per"]=i["Gk_Per"]
                session["Gk_Time_Taken"]=i["Gk_Time_Taken"]
                session["Gk_date_exam"]=i["Gk_date_exam"]
                session["chem_Mark"]=i["chem_Mark"]
                session["chem_Per"]=i["chem_Per"]
                session["chem_Time_Taken"]=i["chem_Time_Taken"]
                session["chem_date_exam"]=i["chem_date_exam"]
                session["Geo_Mark"]=i["Geo_Mark"]
                session["Geo_Per"]=i["Geo_Per"]
                session["Geo_Time_Taken"]=i["Geo_Time_Taken"]
                session["Geo_date_exam"]=i["Geo_date_exam"]
                session["Eng_Mark"]=i["Eng_Mark"]
                session["Eng_Per"]=i["Eng_Per"]
                session["Eng_Time_Taken"]=i["Eng_Time_Taken"]
                session["Eng_date_exam"]=i["Eng_date_exam"]
                if i["Email"]==email :
                    if i["Password"]==password:
                        return render_template("home.html", data=data["student registration"], email=email,fname=session["Firstname"] )
        return render_template("login.html" ,message=message)

@app.route("/caution", methods=["POST", "GET"])
def caution():
    if check_session():
        return render_template("caution.html")  
@app.route("/caution2" , methods=["POST", "GET"])  
def cau():
    if check_session():
        data = mcq_utils.read_json(file)
        if request.method=="POST":
            passwrd=request.form["pasword"] 
            mesage="only owner / admin can open this section" 
            if passwrd=="rnaveen2520@":
                return render_template("mcq2.html",  data=data["student registration"]) 
            else:
                return render_template("caution.html",mesage=mesage)
        return render_template("home.html")     

@app.route("/forgot" , methods=["POST" , "GET"])  
def forgot():
    return render_template("forgot.html")

@app.route("/sentotp" , methods=["POST" , "GET"])
def otp():
    if check_session():
        data = mcq_utils.read_json(file)
        num="0105"
        mes=""
        if request.method=="POST":
            email=request.form["email"]
            mes="your email id is incorrect / did not register / dont recognize"
            for i in data["student registration"] : 
                if i["Email"]==email:
                    return render_template("otp.html", num=num)
                else:
                    return render_template("forgot.html" , mes=mes)
        return render_template("login.html")
    
@app.route("/help" , methods=["POST" , "GET"])
def help():
    if check_session():
        data = mcq_utils.read_json(file)
        for i in data["student registration"]:
            session["Firstname"]=i["Firstname"]
            return render_template("help.html", fname=session["Firstname"])
@app.route("/readmore")
def read():
    return render_template("readmore.html")        
     
@app.route("/quizfrontpage")
def quizfrontpage():
    title="General Knowledge"
    return render_template("frontpage.html", title=title)     

@app.route("/quizfrontpage2")
def quizfrontpage2():
    title="Chemistry"
    return render_template("frontpage2.html" , title=title)

@app.route("/quizfrontpage3")
def quizfrontpage3():
    title="Geology"
    return render_template("frontpage3.html" , title=title)

@app.route("/quizfrontpage4")
def quizfrontpage4():
    title="English"
    return render_template("frontpage4.html" , title=title)

@app.route("/mcq")
def mcq():
    session['start_time'] = datetime.datetime.now()
    session['attend_date'] = datetime.date.today()
    return render_template("quiz.html", quiz=quiz_data1)

@app.route("/mcq2")
def mcq2():
    session['start_time'] = datetime.datetime.now()
    session['attend_date'] = datetime.date.today()
    return render_template("quiz2.html", quiz=quiz_data2)

@app.route("/mcq3")
def mcq3():
    session['start_time'] = datetime.datetime.now()
    session['attend_date'] = datetime.date.today()
    return render_template("quiz3.html", quiz=quiz_data3)

@app.route("/mcq4")
def mcq4():
    session['start_time'] = datetime.datetime.now()
    session['attend_date'] = datetime.date.today()
    return render_template("quiz4.html", quiz=quiz_data4)

@app.route("/quiz",methods=["POST"])  
def quiz_redirect():
    end_time = datetime.datetime.now()
    elapsed_time = end_time - session.get('start_time')
    attend_date = session.get('attend_date')
    msg1="Outstanding"
    msg2="Very good"
    msg3="good"
    msg4="Average"
    msg5="Fail"
    
    # print(request.form["country"])
    # print(request.form["planet"])
    score = 0
    for question in quiz_data1["questions"]:
        for ans in question['answers']:
            if(ans['correct']=="True"):
                crct_ans=ans['text']
        if(request.form[question['answers'][0]['name']])==crct_ans:
            score+=2
        else:
            score-=1 
    per=score / 30 * 100
    data = mcq_utils.read_json(file)
    for i in data["student registration"] :
       if i["Firstname"]==session["Firstname"]:
        session["Gk_Mark"]=i["Gk_Mark"]
        session["Gk_Per"]=i["Gk_Per"]
        session["Gk_Time_Taken"]=i["Gk_Time_Taken"]
        session["Gk_date_exam"]=i["Gk_date_exam"]
        i["Gk_Mark"]=str(score)
        i["Gk_Per"]=str(per)
        i["Gk_Time_Taken"]= elapsed_time
        i["Gk_date_exam"]=attend_date
    with open('studreg.json', 'w') as json_file:
        json.dump(data, json_file, default=str, indent=4)
    if per>=90:
        return render_template("results.html" , msgg=msg1 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)
    elif per>=75: 
        return render_template("results.html" , msgg=msg2 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)   
    elif per>=60:
        return render_template("results.html" , msgg=msg3 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)
    elif per>=45:
        return render_template("results.html" , msgg=msg4 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)   
    else:
        return render_template("results.html" , msgg=msg5 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)           

@app.route("/quiz2",methods=["POST"])  
def quiz_redirect2():
    end_time = datetime.datetime.now()
    elapsed_time = end_time - session.get('start_time')
    attend_date = session.get('attend_date')
    msg1="Outstanding"
    msg2="Very good"
    msg3="good"
    msg4="Average"
    msg5="Fail"
    
    # print(request.form["country"])
    # print(request.form["planet"])
    score = 0
    for question in quiz_data2["questions"]:
        for ans in question['answers']:
            if(ans['correct']=="True"):
                crct_ans=ans['text']
        if(request.form[question['answers'][0]['name']])==crct_ans:
            score+=2
        else:
            score-=1 
    per=score / 30 * 100
    data = mcq_utils.read_json(file)
    for i in data["student registration"] :
       if i["Firstname"]==session["Firstname"]:
        session["chem_Mark"]=i["chem_Mark"]
        session["chem_Per"]=i["chem_Per"]
        session["chem_Time_Taken"]=i["chem_Time_Taken"]
        session["chem_date_exam"]=i["chem_date_exam"]
        i["chem_Mark"]=str(score)
        i["chem_Per"]=str(per)
        i["chem_Time_Taken"]= elapsed_time
        i["chem_date_exam"]=attend_date
    with open('studreg.json', 'w') as json_file:
        json.dump(data, json_file, default=str, indent=4)
    if per>=90:
        return render_template("results.html" , msgg=msg1 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)
    elif per>=75: 
        return render_template("results.html" , msgg=msg2 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)   
    elif per>=60:
        return render_template("results.html" , msgg=msg3 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)
    elif per>=45:
        return render_template("results.html" , msgg=msg4 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)   
    else:
        return render_template("results.html" , msgg=msg5 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)           
    
    
@app.route("/quiz3",methods=["POST"])  
def quiz_redirect3():
    end_time = datetime.datetime.now()
    elapsed_time = end_time - session.get('start_time')
    attend_date = session.get('attend_date')
    msg1="Outstanding"
    msg2="Very good"
    msg3="good"
    msg4="Average"
    msg5="Fail"
    
    # print(request.form["country"])
    # print(request.form["planet"])
    score = 0
    for question in quiz_data3["questions"]:
        for ans in question['answers']:
            if(ans['correct']=="True"):
                crct_ans=ans['text']
        if(request.form[question['answers'][0]['name']])==crct_ans:
            score+=2
        else:
            score-=1 
    per=score / 30 * 100
    data = mcq_utils.read_json(file)
    for i in data["student registration"] :
       if i["Firstname"]==session["Firstname"]:
        session["Geo_Mark"]=i["Geo_Mark"]
        session["Geo_Per"]=i["Geo_Per"]
        session["Geo_Time_Taken"]=i["Geo_Time_Taken"]
        session["Geo_date_exam"]=i["Geo_date_exam"]
        i["Geo_Mark"]=str(score)
        i["Geo_Per"]=str(per)
        i["Geo_Time_Taken"]= elapsed_time
        i["Geo_date_exam"]=attend_date
    with open('studreg.json', 'w') as json_file:
        json.dump(data, json_file, default=str, indent=4)
    if per>=90:
        return render_template("results.html" , msgg=msg1 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)
    elif per>=75: 
        return render_template("results.html" , msgg=msg2 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)   
    elif per>=60:
        return render_template("results.html" , msgg=msg3 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)
    elif per>=45:
        return render_template("results.html" , msgg=msg4 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)   
    else:
        return render_template("results.html" , msgg=msg5 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)           
        

@app.route("/quiz4",methods=["POST"])  
def quiz_redirect4():
    end_time = datetime.datetime.now()
    elapsed_time = end_time - session.get('start_time')
    attend_date = session.get('attend_date')
    msg1="Outstanding"
    msg2="Very good"
    msg3="good"
    msg4="Average"
    msg5="Fail"
    
    # print(request.form["country"])
    # print(request.form["planet"])
    score = 0
    for question in quiz_data4["questions"]:
        for ans in question['answers']:
            if(ans['correct']=="True"):
                crct_ans=ans['text']
        if(request.form[question['answers'][0]['name']])==crct_ans:
            score+=2
        else:
            score-=1 
    per=score / 30 * 100
    data = mcq_utils.read_json(file)
    for i in data["student registration"] :
       if i["Firstname"]==session["Firstname"]:
        session["Eng_Mark"]=i["Eng_Mark"]
        session["Eng_Per"]=i["Eng_Per"]
        session["Eng_Time_Taken"]=i["Eng_Time_Taken"]
        session["Eng_date_exam"]=i["Eng_date_exam"]
        i["Eng_Mark"]=str(score)
        i["Eng_Per"]=str(per)
        i["Eng_Time_Taken"]= elapsed_time
        i["Eng_date_exam"]=attend_date
    with open('studreg.json', 'w') as json_file:
        json.dump(data, json_file, default=str, indent=4)
    if per>=90:
        return render_template("results.html" , msgg=msg1 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)
    elif per>=75: 
        return render_template("results.html" , msgg=msg2 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)   
    elif per>=60:
        return render_template("results.html" , msgg=msg3 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)
    elif per>=45:
        return render_template("results.html" , msgg=msg4 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)   
    else:
        return render_template("results.html" , msgg=msg5 , per=per, elapsed_time=elapsed_time, attend_date=attend_date)           
        


    
@app.route("/nextpage.html") 
def next_page():
    msg="sorry....out of time...!!!"
    return render_template("results.html", msg=msg) 


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)   