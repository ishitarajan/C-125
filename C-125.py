from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homePage():
    return "Welcome!"

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/confirm', methods = ['POST'])
def confirm():
    if request.method == 'POST':
        n = request.form.get("name")
        a = request.form.get("age")
        return render_template("confirm.html", name = n, age=a)

if __name__ == "__main__":
    app.run(debug = True)