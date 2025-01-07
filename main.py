from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello World!</p>'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/about')
def about_us():
	return 'Contact: correct_email@mail.com Phone: 987-654-321'

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=True)
