from flask import Flask, render_template
from models import init_db
from routes.feedback import feedback_bp
# from routes.admin import admin_bp
from routes.store import store_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'

init_db()

app.register_blueprint(feedback_bp)
# app.register_blueprint(admin_bp)
app.register_blueprint(store_bp)

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)