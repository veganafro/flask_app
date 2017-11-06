from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import os
import urlparse
import psycopg2

app = Flask(__name__,
    template_folder="templates",
    static_folder="static"
)

social_data = [
    {
        'social_site': 'LinkedIn',
        'url': 'https://linkedin.com/in/jeremymuhia',
        'img_location': 'linkedin.svg'
    },
    {
        'social_site': 'Quantopian',
        'url': 'https://www.quantopian.com/users/586da5ab0c96877426000182',
        'img_location': 'quantopian.png'
    },
    {
        'social_site': 'Github',
        'url': 'https://github.com/veganafro',
        'img_location': 'github.svg'
    }
]

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
        return render_template('index.html', social_data=social_data)
    except:
        return redirect('/error'), 200

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    try:
        if request.method == 'POST':
            name = request.form['name']
            email_address = request.form['email_address']
            message = request.form['message']
            # do something using maybe a self built api to send an email
            return redirect('/contact'), 200
        elif request.method == 'GET':
            return render_template('contact.hmtl', social_data=social_data), 200
    except:
        return redirect('/error'), 404

@app.route('/social')
def social():
    try:
        return render_template('social.html', social_data=social_data), 200
    except:
        return redirect('/error'), 404

@app.route('/about')
def about():
    try:
        return render_template('about.html', social_data=social_data), 200
    except:
        return redirect('/error'), 404

@app.route('/error')
def error():
    return render_template('error.html', social_data=social_data), 404


if __name__ == '__main__':
    app.run(debug=True)
