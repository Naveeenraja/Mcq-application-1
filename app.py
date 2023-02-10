from flask import Flask, render_template, request, redirect,session
from flask_session import Session
import datetime
import json 

# Create a Flask app
app=Flask(__name__)
app.config["SECRET_KEY"]="somekey"
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

# Read the JSON file
with open("quiz.json", "r") as file:
    quiz_data = json.load(file)
   

# Create a route for the quiz page
@app.route("/")
def quiz_page():
    return render_template("frontpage.html")

@app.route("/mcq")
def mcq():
    session['start_time'] = datetime.datetime.now()
    session['attend_date'] = datetime.date.today()
    return render_template("quiz.html", quiz=quiz_data)


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
    for question in quiz_data["questions"]:
        for ans in question['answers']:
            if(ans['correct']=="True"):
                crct_ans=ans['text']
        if(request.form[question['answers'][0]['name']])==crct_ans:
            score+=2
        else:
            score-=1 
    per=score / 30 * 100
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

# Create a route to handle the form submission and check the answers
# @app.route("/check_answers", methods=["POST"])
# def check_answers():
#     score = 0
#     for i, question in enumerate(quiz_data["questions"]):
#         user_answer = request.form["question" + str(i)]
#         for j, answer in enumerate(question["answers"]):
#             if j == int(user_answer) and answer["correct"]:
#                 score += 1
#     return render_template("results.html", score=score, total_questions=len(quiz_data["questions"]))

if __name__=="__main__":
    app.run(debug=True)