from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/store")
def store():
    return render_template("store.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")




if __name__ == '__main__':
    app.run()