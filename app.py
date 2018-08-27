from flask import (Flask, request, render_template,
                   session, flash, redirect, url_for)
from info import projects, skills, tools


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', projects=projects,
                           skills=skills, tools=tools)


if __name__ == '__main__':
    app.run(port=8000, debug=False)
