from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/testing')
def testing():
    return render_template('testing.html')

if __name__ == '__main__':

    app.run(debug=True)