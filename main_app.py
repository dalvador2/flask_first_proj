from flask import Flask
app = Flask(__name__)

@app.route("/<name>")
def hello_word(name):
    print(name)
    return f"<p>hello world {name}</p>"
