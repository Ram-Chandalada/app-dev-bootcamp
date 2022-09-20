from flask import Flask,render_template,redirect


app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY='ops_digital_asset'
)

@app.route('/',methods=['GET','POST'])
def dashboard():
    user={"name":"Ram"}
    return render_template("dashboard.html",user=user)

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html")

 
if __name__ == "__main__":
    app.run(host="0.0.0.0")