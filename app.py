
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    secret_number = random.randint(1, 10)   # NEW number every time
    user_guess = int(request.form['number'])

    if user_guess == secret_number:
        result = f"🎉 Correct! The number was {secret_number}"
    elif user_guess > secret_number:
        result = f"🔼 Too High! The number was {secret_number}"
    else:
        result = f"🔽 Too Low! The number was {secret_number}"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


