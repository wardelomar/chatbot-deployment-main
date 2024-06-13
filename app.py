# app.py
from flask import  request
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response
from forms import TodoForm
from flask_wtf.csrf import CSRFProtect
from datetime import datetime
from flask_pymongo import PyMongo
from flask import redirect ,flash

app = Flask(__name__)
app.config["SECRET_KEY"]="9bcff7180b57ea1e51f18de2b568a7e2556d1f5e"
csrf = CSRFProtect(app)

app.config["MONGO_URI"]="mongodb+srv://wardalomar2001:ZWmeiVdCRnmNM97O@cluster0.xwgajlf.mongodb.net/data?retryWrites=true&w=majority&appName=Cluster0"
#setup mongo
mongo_client= PyMongo(app)
db=mongo_client.db

@app.get("/")
def index_get():
    return render_template("index.html")

@app.get("/login")
def login():
    return render_template("login.html")

#@app.route("/home")
#def get_cust():
#    custs=[]
#    for cust in db.todo_flask.find().sort("amamlanma tarihi", -1):
#        cust["_id"]= str(cust["_id"])
#        cust["amamlanma tarihi"]= cust["amamlanma tarihi"].strftime("%d %b %Y %H:%M%S")
#        custs.append(cust)
#    return render_template("view_elements.html",title="admin page", custs=custs)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cust_name = request.form.get("name")
        cust_phone = request.form.get("phone")
        cust_personal = request.form.get("person")
        cust_date = request.form.get("date")
        cust_time = request.form.get("time")
        message = request.form.get("message")

        db.todo_flask.insert_one({
            "name": cust_name,
            "phone": cust_phone,
            "personal": cust_personal,
            "date":cust_date,
            "time":cust_time,
            "message":message,
            "amamlanma tarihi": datetime.utcnow()
        })
        flash("Ekleme tamamlandı", "success")
        return redirect("/")

    return render_template("index.html")

@app.route("/add", methods=["POST","GET"])
def add_cust():
    if request.method== "POST":
        form=TodoForm(request.form)
        cust_name= form.name.data
        cust_phone=form.phone.data
        cust_personal=form.personal.data
        cust_date=form.date.data
        cust_time=form.time.data
        message=form.message.data
        

        db.todo_flask.insert_one({
            "name": cust_name,
            "phone": cust_phone,
            "personal": cust_personal,
            "date":cust_date,
            "time":cust_time,
            "message":message,
            "amamlanma tarihi": datetime.utcnow()
        })
        flash("amamlanma tarihi","seccess")
        return redirect("/add_cust")
    else:
        form=TodoForm()

    return render_template("add_cust.html", form=form)

#@app.post("/predict")
#def predict():
#    try:
#        data = request.get_json()
#        text = data.get("message")
#        print(f"Received message: {text}")  # Debugging line
#        response = get_response(text)
#        print(f"Generated response: {response}")  # Debugging line
#        message = {"answer": response}
#        return jsonify(message)
#    except Exception as e:
#        print(f"Error: {e}")
#        return jsonify({"answer": "An error occurred"}), 500
@app.post("/predict")
def predict():
    try:
        data = request.get_json()
        text = data.get("message")
        print(f"Gelen mesaj: {text}")  # Hata ayıklama için log satırı
        response = get_response(text)
        print(f"Oluşturulan cevap: {response}")  # Hata ayıklama için log satırı
        message = {"answer": response}
        return jsonify(message)
    except Exception as e:
        print(f"Hata: {e}")
        return jsonify({"answer": "Bir hata oluştu"}), 500

if __name__ == "__main__":
    app.run(debug=True)

