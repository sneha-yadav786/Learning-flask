from flask import Flask,render_template,request, redirect, url_for,flash
from forms import RegistrationForm
app=Flask(__name__)
app.secret_key="ddfd"
@app.route('/', methods=['GET','POST'])
def submit():
    form=RegistrationForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data

        flash("welcome {name}!, You successfully Registered." , "success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)
@app.route('/success')
def success():
    return render_template("success.html")
    

if __name__ == "__main__":
    app.run(debug=True)
