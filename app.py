from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Railway!"

if __name__ == "__main__":
    from os import environ
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))
