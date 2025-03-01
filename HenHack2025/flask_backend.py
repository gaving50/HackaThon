from flask import Flask, render_template, request
from AI import make_gemini_request

app = Flask(__name__)
data=""

@app.route('/')
def home():
    return render_template('index.html')    # render index.html

@app.route('/submit', methods=['POST'])  
def submit():
    # get the data from the form
    data=""
    data = request.form['inputText']
    response = make_gemini_request(data)
    return str(response.text)
    


