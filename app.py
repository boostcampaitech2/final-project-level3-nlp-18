from flask import Flask, request, render_template
from translator import interactive_one

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    original_text = request.form['text']
    translated_text = interactive_one.cli_main(original_text)

    return render_template(
        'result.html',
        original_text=original_text,
        translated_text=translated_text
    )

@app.route('/', methods=['GET'])
def result():
    return render_template('result.html')