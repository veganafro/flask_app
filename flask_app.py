from flask import Flask, render_template, request, redirect
import os
import urlparse
import psycopg2


app = Flask(__name__, template_folder="templates", static_folder="static")

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

db = conn.cursor()

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except:
        return redirect('/error')

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    try:
        if request.method == 'POST':
            name = request.form['name']
            email_address = request.form['email_address']
            message = request.form['message']
            #do something using smtplib to send an email
            return redirect('/contact')
        elif request.method == 'GET':
            render_template('contact.hmtl')
    except:
        return redirect('/error')

@app.route('/social')
def social():
    try:
        render_template('social.html')
    except:
        return redirect('/error')

@app.route('/about')
def about():
    try:
        render_template('about.html')
    except:
        return redirect('/error')

@app.route('/error')
def error():
    render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)