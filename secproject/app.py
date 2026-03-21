from flask import Flask,render_template,request, redirect, url_for
app=Flask(__name__)
app.secret_key="ddfd"
@app.route('/', methods=['GET','POST'])
def submit():
    print(request.method)
    if request.method=="POST":
        user=request.form.get('user')
        feedback=request.form.get('feedback')
        rating=request.form.get('rating')
        return render_template("thankyou.html", name=user,  feed=feedback, rating=rating)
    return render_template("feedback.html")

if __name__ == "__main__":
    app.run(debug=True)
