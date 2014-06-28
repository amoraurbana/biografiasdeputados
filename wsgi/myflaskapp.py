from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "melhorar!"




@app.route("/bethoven")
def bebe():
    return "<h1>Bethoven!</h1>"







if __name__ == "__main__":
    app.run()

