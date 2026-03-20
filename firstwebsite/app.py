from flask import Flask, render_template,session,request,Response,url_for,redirect
app=Flask(__name__)
app.secret_key="ssssss"
@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username=="prateek" and password=="786":
            session["user"]=username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid username or password ❌.")
    return render_template("login.html")

@app.route('/about')
def About():
    return render_template("About.html")
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")
@app.route('/logout')
def logout():
    session.pop("user",None)
    return redirect(url_for("home"))
if __name__== "__main__":
    app.run(debug=True)