from flask import Flask, render_template, request, redirect
#import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        name = request.form['Name']
        return render_template("index.html", name)
    except:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)