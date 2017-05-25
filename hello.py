from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/user/<name>')
def user(name):
    return 'hello %s' % name

@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return 'browser is %s' % user_agent



if __name__ == '__main__':
    app.run(debug=True)
