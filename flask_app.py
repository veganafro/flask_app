from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import os
import urlparse
import psycopg2

app = Flask(__name__, template_folder="templates", static_folder="static")

def connection():
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
    return db

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
            return redirect('/contact'), 200
        elif request.method == 'GET':
            return render_template('contact.hmtl'), 200
    except:
        return redirect('/error'), 404

@app.route('/social')
def social():
    try:
        return render_template('social.html'), 200
    except:
        return redirect('/error'), 404

@app.route('/about')
def about():
    try:
        return render_template('about.html'), 200
    except:
        return redirect('/error'), 404

@app.route('/error')
def error():
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(debug=True)