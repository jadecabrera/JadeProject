from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/transaction')
def transaction():
    return render_template('transaction.html')

@app.route('/redeem')
def redeem():
    return render_template('redeem.html')

if __name__ == '__main__':
    app.run()
