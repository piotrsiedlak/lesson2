from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello World!</p>'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/about')
def about_us():
	return 'Contact: me@mail.com Phone: 123-456-789'

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=True)
