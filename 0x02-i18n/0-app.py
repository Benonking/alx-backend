from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def dell():
    title = "Welcome to Holberton"
    h1 = "Hello World"
    return render_template('0-index.html', title=title, h1=h1)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
