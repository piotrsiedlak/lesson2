from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/about')
def presentation():
	return 'Contact: me@mail.com \n Phone: 123-456-789'

if __name__ == '__main__':

    app.run(debug=True)
