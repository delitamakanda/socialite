from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	#return '<h1>app work! Your browser is %s</h1>' % user_agent
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	user = load_user(name):
	if not user:
		abort(404)
	#return '<h1>app work %s!</h1>' % name
	return render_template('user.html', name=name)

@app.errorhandler(400):
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500):
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	app.run(debug=True)
