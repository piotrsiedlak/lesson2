from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello World!</p>'

@app.route('/about')
def about_us():
	return '    <h1>Contact Us</h1>
		    <p>Phone: <a href="tel:+1234567890">+1 (234) 567-890</a></p>
    		    <p>Email: <a href="mailto:info@example.com">info@example.com</a></p>
		'

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
