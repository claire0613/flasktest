from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator


@app.route('/')
def index():
    return render_template("index.html")
# localhost:5000/user/john


@app.route('/user/<name>')
def user(name):
    return "<h1>Hi!!%s<h1>" % name

# invalid URL


@app.errorhandler(404)
def page_not_fount(e):
    return render_template('erro.html', 404)
