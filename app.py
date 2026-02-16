from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/customize', methods=['POST'])
def customize():
    resume_text = request.form['resume']
    cover_letter_text = request.form['cover_letter']
    # Add customization logic here
    return render_template('customized.html', resume=resume_text, cover_letter=cover_letter_text)

if __name__ == '__main__':
    app.run(debug=True)