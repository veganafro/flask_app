from flask import Flask, render_template, request, redirect
import os
import urlparse
import psycopg2

app = Flask(__name__)

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["postgres://cqjvgnkkjlqgri:K5tMTNqXIPgP1N1-OgZeacAi8K@ec2-54-243-45-168.compute-1.amazonaws.com:5432/dfubavudjcgt9d"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

db = conn.cursor()

#db.execute("SOME PgSQL COMMANDS", some_variables)

data = db.fetchall()

db.commit()

db.close()

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except:
        return redirect('/error')

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email_address = request.form['email_address']
        message = request.form['message']
        #do something using smtplib to send an email
        return redirect('/contact')
    elif request.method == 'GET':
        render_template('contact.hmtl')

@app.route('/social')
def social():
    render_template('social.html')

@app.route('/about')
def about():
    render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)