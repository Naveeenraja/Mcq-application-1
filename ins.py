from flask import Flask,render_template,request,redirect,session
from flask_session import Session
import data.mcqutil as mcq_utils
import json
from datetime import date, timedelta
file ="customers.json"


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
        session.pop("code_number" , None)
        session.pop("Firstname" , None) 
    return redirect("/")  

@app.route("/", methods=["POST" , "GET"])
def index():
    return render_template("index.html")   

@app.route("/register_page", methods=["POST" , "GET"])
def register_page():
    return render_template("register.html")

@app.route("/login_page", methods=["POST" , "GET"])
def login_page():
    return render_template("login.html")   

@app.route("/service_page", methods=["POST" , "GET"])
def service_page():
    return render_template("services.html") 

@app.route("/contact_page", methods=["POST" , "GET"])
def contact_page():
    return render_template("contact.html") 

@app.route("/about_page", methods=["POST" , "GET"])
def about_page():
    return render_template("about.html") 

@app.route("/register", methods=["POST" , "GET"])
def reg():
    data = mcq_utils.read_json(file)
    if request.method=="POST":
        fname=request.form["firstName"]
        email= request.form["email"]
        phone= request.form["phoneNumber"]
        if fname in session:
            return render_template("register.html",msg="your name already registered!!!!!")
        if email in session:
            return render_template("register.html", msg1="your email already registered")
        if phone in session:
            return render_template("register.html", msg2="your phone number already registered")
        session[fname]=False
        session[email]=False
        session[phone]=False
        length=len(data["customers"])
        code=length + 100984 
        fname=request.form["firstName"]
        lname=request.form["lastname"]
        email= request.form["email"]
        phone= request.form["phoneNumber"]
        password= request.form["password"]
        list_of_customers={
            "code_number" : code,
            "Firstname" : fname,
            "Lastname"  : lname,
            "phone" : phone,
            "Email" : email,
            "Password" : password,
            "Health Insurance Policy Id": "", 
            "Vehicle Insurance Policy Id": "",
            "Life Insurance Policy Id":"" ,
            "Middlename" : ""  ,
            "Father / Husbandname" : "",
            "Surname" : "",
            "Full Name" : "",
            "nominee" : "" ,
            "Type of relation" : "" ,
            "Age" : "" ,
            "Date of Birth" : "",
            "Gender" : "",
            "Address1" : "",
            "Address2" : "",
            "District" : "",
            "State" : "",
            "Pincode" : "",
            "phone2" : "",
            "email2" : "",  
            "Policy Type" : "",
            "Id Type" : "",
            "Id Number" : "",
            "Premium" : "",
            "Amount" : "",
            "Next Premium Date" : "",
            "Policy Type2" : "",
            "Id Type2" : "",
            "Id Number2" : "",
            "Premium2" : "",
            "Amount2" : "",
            "Next Premium Date2" : "",
            "Policy Type3" : "",
            "Premium3" : "",
            "Type of vehicle" : "",
            "Vehicle number" : "",
            "DL / RC Num" : "",
            "Amount3" : "",
            "Next Premium Date3" : ""
        }
        data["customers"].append(list_of_customers)
        mcq_utils.write_json(file,data)
        msg= fname + " Your registration has been completed successfully !! " +"your code number is :" + str(code)
        msg2="your code number is :" + str(code)
        data = mcq_utils.read_json(file)
        return render_template("login.html",data=data["customers"],msg=msg )
    # return render_template("mcq2.html", data=data["student registration"])
    
@app.route("/login", methods=["GET" , "POST"])
def login():
    # if check_session():
        data = mcq_utils.read_json(file)
        message=""
        if request.method=="POST":                                                   
            code=int(request.form["code"])
            password=request.form["password"]
            message="incorrect password / code Number" 
            for i in data["customers"] : 
                session['user']=i['Firstname']
                session["firstname"]=i["Firstname"]
                session["email"]=i["Email"]
                session["lastname"]=i["Lastname"]
                session["phone"]=i["phone"]
                session["code_number"]=i["code_number"]
                session["Life Insurance Policy Id"]=i["Life Insurance Policy Id"]
                session['Middlename']=i['Middlename']
                session['Surname']= i['Surname']
                session['Father / husband name']=i['Father / Husbandname']
                session['nominee']=i['nominee']
                session['Type of Relation']=i['Type of relation']
                session['Age']=i['Age']
                session['Date of Birth']=i['Date of Birth']
                session['Gender']=i['Gender']
                session['Address1']=i['Address1']
                session['Address2']=i['Address2']
                session['District']= i['District']
                session['State']=i['State']
                session['Pincode']=i['Pincode']
                session['phone2']=i['phone2']
                session['email2']=i['email2']
                session['Policytype']=i['Policy Type']
                session['IDtype']=i['Id Type']
                session['Id Number']=i['Id Number']
                session['Premium']=i['Premium']
                session['Amount']=i['Amount']
                session['Next Premium Date']=i['Next Premium Date']
                session['Full Name']=i['Full Name']
                session['Life Insurance Policy Id']=i['Life Insurance Policy Id']
                session['Policytype2']=i['Policy Type2']
                session['IDtype2']=i['Id Type2']
                session['Id Number2']=i['Id Number2']
                session['Premium2']=i['Premium2']
                session['Amount2']=i['Amount2']
                session['Next Premium Date2']=i['Next Premium Date2']
                session['Health Insurance Policy Id']=i['Health Insurance Policy Id']
                session['Policytype3']=i['Policy Type3']
                session['Premium3']=i['Premium3']
                session['Type of vehicle']=i['Type of vehicle']
                session['Amount3']=i['Amount3']
                session['Vehicle number']=i['Vehicle number']
                session['DL / RC Num']=i['DL / RC Num']
                session['Next Premium Date3']=i['Next Premium Date3']
                session['Vehicle Insurance Policy Id']=i['Vehicle Insurance Policy Id']
                if i["code_number"]==code :
                    
                    if i["Password"]==password:
                        
                        return render_template("sucess.html")
        return render_template("login.html" ,message=message)

@app.route("/gotodashboard")
def gotodashboard():
    msg="Life"
    if check_session():
        data=mcq_utils.read_json(file)
        for i in data['customers']:
            if i['Firstname'] == session['firstname']:
                session['Policytype']=i['Policy Type']
                session['Life Insurance Policy Id']=i['Life Insurance Policy Id']
                session['Premium']=i['Premium']
                session['Amount']=i['Amount']
                session['Next Premium Date']=i['Next Premium Date']
                session['Full Name']=i['Full Name']
                session['nominee']=i['nominee']
        return render_template("dashboard.html", msg=msg,data=data["customers"],premiumdate=session['Next Premium Date'] , fname=session['firstname'] ,amount= session['Amount'],premium= session['Premium'], policyholdername= session['Full Name'],  policytype=session['Policytype'] ,policyid=session["Life Insurance Policy Id"] ,nominee=session['nominee'] )

@app.route("/gotovehicle")
def gotovehicle():
    msg2="Vehicle"
    if check_session():
        data=mcq_utils.read_json(file)
        for i in data['customers']:
            if i['Firstname'] == session['firstname']:
                session['Policytype3']=i['Policy Type3']
                session['Vehicle Insurance Policy Id']=i['Vehicle Insurance Policy Id']
                session['Type of vehicle"']=i['Type of vehicle']
                session['Amount3']=i['Amount3']
                session['Next Premium Date3']=i['Next Premium Date3']
                session['Full Name']=i['Full Name']
                session['Vehicle number']=i['Vehicle number']
                session['DL / RC Num']=i['DL / RC Num']
        return render_template("dashboard2.html",msg2=msg2, fname=session['firstname'],premiumdate=session['Next Premium Date3']  ,amount= session['Amount3'],vehicle= session['Type of vehicle"'], policyholdername= session['Full Name'],  policytype=session['Policytype3'] ,policyid=session["Vehicle Insurance Policy Id"] ,number=session['Vehicle number'], dl= session['DL / RC Num'])

@app.route("/gotohealth")
def gotohealth():
    msg1="Health"
    if check_session():
        data=mcq_utils.read_json(file)
        for i in data['customers']:
            if i['Firstname'] == session['firstname']:
                session['Policytype2']=i['Policy Type2']
                session['Health Insurance Policy Id']=i['Health Insurance Policy Id']
                session['Premium2']=i['Premium2']
                session['Amount2']=i['Amount2']
                session['Next Premium Date2']=i['Next Premium Date2']
                session['Full Name']=i['Full Name']
                session['nominee']=i['nominee']
        return render_template("dashboard3.html",msg1=msg1,premiumdate=session['Next Premium Date2'] , fname=session['firstname'] ,amount= session['Amount2'],premium= session['Premium2'], policyholdername= session['Full Name'],  policytype=session['Policytype2'] ,policyid=session["Health Insurance Policy Id"] ,nominee=session['nominee'] )

@app.route("/new_policy2")
def new_policy2():
    if check_session():
        return render_template("reg2.html",fname= session["firstname"], code=session["code_number"], email=session["email"], phone=session["phone"],mname=session['Middlename'],sname=session['Surname'], fhname=session['Father / husband name'],age=session["Age"],dob= session['Date of Birth'],gender=session['Gender'],add2=session['Address2'],add=session['Address1'], dis=session['District'], state= session['State'], pin=session['Pincode'], rel=session['Type of Relation'])

@app.route("/new_policy3" , methods=["POST" , "GET"])
def new_policy3():
    if check_session():
        return render_template("reg3.html", fname= session["firstname"], code=session["code_number"], email=session["email"], phone=session["phone"],mname=session['Middlename'],sname=session['Surname'], fhname=session['Father / husband name'],age=session["Age"],dob= session['Date of Birth'],gender=session['Gender'], nominee=session['nominee'],add2=session['Address2'],add=session['Address1'], dis=session['District'], state= session['State'], pin=session['Pincode'], rel=session['Type of Relation'])

@app.route("/new_policy")
def new_policy():
    if check_session():
        return render_template("reg.html", fname= session["firstname"], code=session["code_number"], email=session["email"], phone=session["phone"],mname=session['Middlename'],sname=session['Surname'], fhname=session['Father / husband name'],age=session["Age"],dob= session['Date of Birth'],gender=session['Gender'], nominee=session['nominee'],add2=session['Address2'],add=session['Address1'], dis=session['District'], state= session['State'], pin=session['Pincode'], rel=session['Type of Relation'])

@app.route("/next_page" , methods=["GET" , "POST"]) 
def next_page():
    if 'user' in session:
        data = mcq_utils.read_json(file)
        if request.method == 'POST':
            for i in data['customers']:
                i['Policy Type']=request.form["policytype"]
                if  i['Policy Type'] in session:
                    return render_template("dashboard.html",msg="Life",premiumdate=session['Next Premium Date']  ,amount= session['Amount'],premium= session['Premium'], policyholdername= session['Full Name'],  policytype=session['Policytype'] ,policyid=session["Life Insurance Policy Id"] ,nominee=session['nominee'],fname= session["firstname"],mesg="your informations already registered!!!!!")
                 
            session[i['Policy Type']]=False
            with open('customers.json') as json_file:
                data = json.load(json_file)
            for i in data['customers']:
                if i['Firstname'] == session['firstname']:
                    i['Policy Type']=request.form["policytype"]
                    i['Middlename']=request.form["middle"]
                    i['Surname']=request.form["surname"]
                    i['Father / Husbandname']=request.form["fhname"]
                    i['nominee']=request.form["nominee"]
                    i['Type of relation']=request.form["relation"]
                    i['Age']=request.form['age']
                    i['Date of Birth']=request.form["dob"]
                    i['Gender'] = request.form['gender']
                    i['Address1']=request.form["address1"]
                    i['Address2']=request.form["address2"]
                    i['District']=request.form["dis"]
                    i['State']=request.form["state"]
                    i['Pincode']=request.form["pin"]
                    i['phone2']=request.form['phone']
                    i['email2']=request.form['email']
                    session['Middlename']=i['Middlename']
                    session['Surname']= i['Surname']
                    session['Father / husband name']=i['Father / Husbandname']
                    session['nominee']=i['nominee']
                    session['Type of Relation']=i['Type of relation']
                    session['Age']=i['Age']
                    session['Date of Birth']=i['Date of Birth']
                    session['Gender']=i['Gender']
                    session['Address1']=i['Address1']
                    session['Address2']=i['Address2']
                    session['District']= i['District']
                    session['State']=i['State']
                    session['Pincode']=i['Pincode']
                    session['phone2']=i['phone2']
                    session['email2']=i['email2']
            with open('customers.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
            return render_template("next.html", fname=session['firstname'], lname=session['lastname'], nominee=session['nominee'],mname= session['Middlename'],sname=session['Surname'],fhname=session['Father / husband name'],relation=session['Type of Relation'], age=session['Age'],dob=session['Date of Birth'],gender=session['Gender'],add1=session['Address1'],add2=session['Address2'],dis=session['District'],state=session['State'],pin=session['Pincode'],phone=session['phone'] and session['phone2'],email=session['email'] and session['email2'])   
@app.route("/edit" , methods=["GET" , "POST"]) 
def edit():
    return render_template("reg.html" , fname= session["firstname"], code=session["code_number"], email=session["email"], phone=session["phone"])   

@app.route("/exit" , methods=["GET" , "POST"])   
def exit():
     return render_template("dashboard.html" ,premiumdate=session['Next Premium Date'] , fname=session['firstname'] ,amount= session['Amount'],premium= session['Premium'], policyholdername= session['Full Name'] ,policyid=session["Life Insurance Policy Id"] ,nominee=session['nominee'])

@app.route("/save" , methods=["GET" , "POST"])   
def save():
    current_date=date.today()
    threemonth= current_date + timedelta(days=90)
    onemonth= current_date + timedelta(days=30)
    msg="Platinum Premuim -Rs. $2256/- per 3 month "
    msg1="Gold Premium - Rs.$1856/- per 3 months"
    msg2="Silver Premium - Rs.$1056/- per 3 months"
    msg3="Bronze Premium - Rs.$956/- per 3 months"
    msg4="Platinum Premium - Rs.$1056/- per month"
    msg5="Gold Premium - Rs.$896/- per  month"
    msg6="Silver Premium - Rs.$446/- per month"
    msg7="Bronze Premium - Rs.$276/- per month"
    return render_template("policy.html", current_date=current_date, threemonth=threemonth ,onemonth=onemonth, fname=session['firstname'], nominee=session['nominee'] , fhname=session['Father / husband name'], msg=msg, msg1=msg1, msg2=msg2, msg3=msg3, msg4=msg4, msg5=msg5, msg6=msg6, msg7=msg7) 


@app.route("/next2" , methods=["GET" , "POST"]) 
def next2():
    current_date=date.today()
    sixmonth = current_date + timedelta(days=180)
    twomonth = current_date + timedelta(days=60)
    if 'user' in session:
        data = mcq_utils.read_json(file)
    if request.method == 'POST':
        for i in data['customers']:
            i['Policy Type2']=request.form["policytype"]
            if  i['Policy Type2'] in session:
                return render_template("dashboard3.html",msg1="Health",premiumdate=session['Next Premium Date2']  ,amount= session['Amount2'],premium= session['Premium2'], policyholdername= session['Full Name'],  policytype=session['Policytype2'] ,policyid=session["Health Insurance Policy Id"] ,nominee=session['nominee'],fname= session["firstname"],mesg="your informations already registered!!!!!")
        session [i['Policy Type2']]=False 
        i['Policy Type2']=request.form["policytype"]   
        session['Policy Type2'] = i['Policy Type2']
        with open('customers.json') as json_file:
            data = json.load(json_file)
        for i in data['customers']:
            if i['Firstname'] == session['firstname']:
                i['Policy Type2']=request.form["policytype"]
                i['Middlename']=request.form["middle"]
                i['Surname']=request.form["surname"]
                i['Father / Husbandname']=request.form["fhname"]
                i['nominee']=request.form["nominee"]
                i['Type of relation']=request.form["relation"]
                i['Age']=request.form['age']
                i['Date of Birth']=request.form["dob"]
                i['Gender'] = request.form['gender']
                i['Address1']=request.form["address1"]
                i['Address2']=request.form["address2"]
                i['District']=request.form["dis"]
                i['State']=request.form["state"]
                i['Pincode']=request.form["pin"]
                i['phone2']=request.form['phone']
                i['email2']=request.form['email']
                session['Middlename']=i['Middlename']
                session['Surname']= i['Surname']
                session['Father / husband name']=i['Father / Husbandname']
                session['nominee']=i['nominee']
                session['Type of Relation']=i['Type of relation']
                session['Age']=i['Age']
                session['Date of Birth']=i['Date of Birth']
                session['Gender']=i['Gender']
                session['Address1']=i['Address1']
                session['Address2']=i['Address2']
                session['District']= i['District']
                session['State']=i['State']
                session['Pincode']=i['Pincode']
                session['phone2']=i['phone2']
                session['email2']=i['email2']
        with open('customers.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return render_template("policy2.html",six=sixmonth,two = twomonth, current_date=current_date, fname=session['firstname'])


@app.route("/next3" ,  methods=["GET" , "POST"])
def next3():
    current_date=date.today()
    sixmonth = current_date + timedelta(days=180)
    threemonth= current_date + timedelta(days=90)
    msg="Rs. $6745.50"
    msg1="Rs. $8745.50"
    msg2="Rs. $3450.25"
    msg3="Rs. $2100.25"
    data = mcq_utils.read_json(file)
    if 'user' in session:
        if request.method == 'POST':
            for i in data['customers']:
                i['Policy Type3']=request.form["policytype"]
                if  i['Policy Type3'] in session:
                    return render_template("dashboard2.html",dl=session['DL / RC Num'], msg2="Vehicle",number=session['Vehicle number'] ,vehicle=session['Type of vehicle'],premiumdate=session['Next Premium Date3'] , fname=session['firstname'] ,amount= session['Amount3'],premium= session['Premium3'], policyholdername= session['Full Name'],  policytype=session['Policytype3'] ,policyid=session["Vehicle Insurance Policy Id"],mesg="your informations already registered!!!!!")
                
            session [i['Policy Type3']]=False
            i['Policy Type3']=request.form["policytype"]
            with open('customers.json') as json_file:
               data = json.load(json_file)
            for i in data['customers']:
                if i['Firstname'] == session['firstname']:
                    i['Policy Type3']=request.form["policytype"]
                    i['Middlename']=request.form["middle"]
                    i['Surname']=request.form["surname"]
                    i['Father / Husbandname']=request.form["fhname"]
                    
                    i['Type of relation']=request.form["relation"]
                    i['Age']=request.form['age']
                    i['Date of Birth']=request.form["dob"]
                    i['Gender'] = request.form['gender']
                    i['Address1']=request.form["address1"]
                    i['Address2']=request.form["address2"]
                    i['District']=request.form["dis"]
                    i['State']=request.form["state"]
                    i['Pincode']=request.form["pin"]
                    i['phone2']=request.form['phone']
                    i['email2']=request.form['email']
                    session['Middlename']=i['Middlename']
                    session['Surname']= i['Surname']
                    session['Father / husband name']=i['Father / Husbandname']
                    session['nominee']=i['nominee']
                    session['Type of Relation']=i['Type of relation']
                    session['Age']=i['Age']
                    session['Date of Birth']=i['Date of Birth']
                    session['Gender']=i['Gender']
                    session['Address1']=i['Address1']
                    session['Address2']=i['Address2']
                    session['District']= i['District']
                    session['State']=i['State']
                    session['Pincode']=i['Pincode']
                    session['phone2']=i['phone2']
                    session['email2']=i['email2']
            with open('customers.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
            return render_template("policyvehi.html",fname=session['firstname'],six=sixmonth,three = threemonth, current_date=current_date,msg=msg,msg1=msg1,msg2=msg2,msg3=msg3)

@app.route("/life" , methods=["GET" , "POST"])  
def life_insurance():
    msg="Life"
    ms="Your Life Insurance registration has been completed successfully!"
    if check_session():
        data=mcq_utils.read_json(file)
        length=len(data["customers"])
        if 'user' in session:
            if request.method == 'POST':
                with open('customers.json') as json_file:
                    data = json.load(json_file)
                for i in data['customers']:
                    if i['Firstname'] == session['firstname']:
                        i['Id Type']=request.form["idtype"]
                        i['Id Number']=request.form["idnumber"]
                        i['Premium']=request.form["policy"]
                        i['Amount']=request.form["type"]
                        i['Full Name']=request.form["name"]
                        i['Life Insurance Policy Id']= length * 324567 * 3
                        i['Next Premium Date']=request.form["type2"]
                        session['Policytype']=i['Policy Type']
                        session['IDtype']=i['Id Type']
                        session['Id Number']=i['Id Number']
                        session['Premium']=i['Premium']
                        session['Amount']=i['Amount']
                        session['Next Premium Date']=i['Next Premium Date']
                        session['Full Name']=i['Full Name']
                        session['Life Insurance Policy Id']=i['Life Insurance Policy Id']
                with open('customers.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                return render_template("dashboard.html", msg=msg,ms=ms, premiumdate=session['Next Premium Date'] , fname=session['firstname'] ,amount= session['Amount'],premium= session['Premium'], policyholdername= session['Full Name'],  policytype=session['Policytype'] ,policyid=session["Life Insurance Policy Id"] ,nominee=session['nominee'])


@app.route("/health" , methods=["GET" , "POST"])  
def health_insurance():
    msg1="Health"
    ms="Your Health Insurance registration has been completed successfully!"
    if check_session():
        data=mcq_utils.read_json(file)
        length=len(data["customers"])
        if 'user' in session:
            if request.method == 'POST':
                with open('customers.json') as json_file:
                    data = json.load(json_file)
                for i in data['customers']:
                    if i['Firstname'] == session['firstname']:
                        i['Id Type2']=request.form["idtype"]
                        i['Id Number2']=request.form["idnumber"]
                        i['Premium2']=request.form["policy"]
                        i['Amount2']=request.form["type"]
                        i['Full Name']=request.form["name"]
                        i['Health Insurance Policy Id']=length * 2131125 * 2
                        i['Next Premium Date2']=request.form["type2"]
                        session['Policytype2']=i['Policy Type2']
                        session['IDtype2']=i['Id Type2']
                        session['Id Number2']=i['Id Number2']
                        session['Premium2']=i['Premium2']
                        session['Amount2']=i['Amount2']
                        session['Next Premium Date2']=i['Next Premium Date2']
                        session['Full Name']=i['Full Name']
                        session['Health Insurance Policy Id']=i['Health Insurance Policy Id']
                with open('customers.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                return render_template("dashboard3.html",ms=ms, msg1=msg1, premiumdate=session['Next Premium Date2'] , fname=session['firstname'] ,amount= session['Amount2'],premium= session['Premium2'], policyholdername= session['Full Name'],  policytype=session['Policytype2'] ,policyid=session["Health Insurance Policy Id"] ,nominee=session['nominee'])

@app.route("/vehicle" , methods=["GET" , "POST"])  
def vehicle_insurance():
    msg2="Vehicle"
    ms="your Vehicle insurance registration has been completed successfully!"
    if check_session():
        data=mcq_utils.read_json(file)
        length=len(data["customers"])
        if 'user' in session:
            if request.method == 'POST':
                with open('customers.json') as json_file:
                    data = json.load(json_file)
                for i in data['customers']:
                    if i['Firstname'] == session['firstname']:
                        
                        i['Type of vehicle']=request.form["vehicletype"]
                        i['Vehicle number']=request.form["number"]
                        i['DL / RC Num']=request.form["dl"]
                        i['Premium3']=request.form["policy"]
                        i['Amount3']=request.form["type"]
                        i['Full Name']=request.form["name"]
                        i['Vehicle Insurance Policy Id']=length * 456346 * 4
                        i['Next Premium Date3']=request.form["type2"]
                        session['Policytype3']=i['Policy Type3']
                        session['Type of vehicle']=i['Type of vehicle']
                        session['Vehicle number']=i['Vehicle number']
                        session['Premium3']=i['Premium3']
                        session['Amount3']=i['Amount3']
                        session['Next Premium Date3']=i['Next Premium Date3']
                        session['Full Name']=i['Full Name']
                        session['DL / RC Num']= i['DL / RC Num']
                        session['Vehicle Insurance Policy Id']= i['Vehicle Insurance Policy Id']
                with open('customers.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                return render_template("dashboard2.html",dl=session['DL / RC Num'],ms=ms, msg2=msg2,number=session['Vehicle number'] ,vehicle=session['Type of vehicle'],premiumdate=session['Next Premium Date3'] , fname=session['firstname'] ,amount= session['Amount3'],premium= session['Premium3'], policyholdername= session['Full Name'],  policytype=session['Policytype3'] ,policyid=session["Vehicle Insurance Policy Id"] )
        


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)  