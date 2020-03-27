from flask import Flask, request, render_template
from suffixexpression import SuffixExpression

import base64

ENV = 'development'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show():
    return render_template('index.html')


## framework here, I have almost make it done here. 
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    expr_encode= request.form['expr']

    expr = base64.b64decode(expr_encode)

    suffix = SuffixExpression()

    ans = suffix.calculate(expr)
    return str(ans)

if __name__ == '__main__':
    app.run()

