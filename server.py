from flask import Flask, render_template, request
import db

app = Flask(__name__)
db.setup()

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name, guestbook=db.get_guestbook())

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get("name")
        comment = request.form.get("text")
        db.add_post(name, comment)
    return render_template('hello.html', name="Visitor", guestbook=db.get_guestbook())
