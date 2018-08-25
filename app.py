from flask import (Flask, request, render_template,
                   session, flash, redirect, url_for)
 
app = Flask(__name__)
 
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(port=8000, debug=True)