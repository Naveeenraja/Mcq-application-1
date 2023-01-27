from flask import Flask,render_template,request,redirect, url_for,session
from flask_session import Session
import data.mcqutil as mcq_utils
file ="studreg.json"
file1 = "mcq.json"
app=Flask(__name__)
app.config["SECRET_KEY"]="somekey"
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

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
        return render_template("mark.html")
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
            
        
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)   