from flask import Flask, request, render_template
from translator import interactive_one, interactive_two

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

@app.route('/second', methods=['GET'])
def second():
    return render_template('second.html')

@app.route('/second', methods=['POST'])
def second_post():
    original_text = request.form['text']
    translated_text = interactive_two.cli_main(original_text)

    return render_template(
        'result_second.html',
        original_text=original_text,
        translated_text=translated_text
    )

@app.route('/', methods=['GET'])
def result():
    return render_template('result.html')

@app.route('/second', methods=['GET'])
def result_second():
    return render_template('result_second.html')