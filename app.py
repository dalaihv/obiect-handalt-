from flask import Flask, render_template

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/')
def index():
    return render_template("lab6.html")

@app.route('/help')
def help_page():
    return render_template("help.html")

if __name__ == "__main__":
    app.run(debug=True)
