from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Example route
@app.route('/')
def index():
    tasks = []  # or fetch from DB
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
