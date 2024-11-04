from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello World!</p>'

@app.route('/about')
def about_us():
	return 'Contact: me@mail.com Phone: 123-456-789'

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
