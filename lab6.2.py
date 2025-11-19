from flask import Flask, redirect, url_for, abort

app = Flask(__name__)

# ---- ROUTES ----
@app.route('/')
def index():
    return "<h1>Hello, this is INDEX page</h1>"

@app.route('/help')
def help_page():
    return "<h1>This is HELP page</h1>"

# ---- REDIRECT ЖИШЭЭ ----
@app.route('/go-help')
def go_help():
    # /go-help → /help хуудас руу чиглэнэ
    return redirect(url_for('help_page'))

# ---- ERROR ЖИШЭЭ ----
@app.route('/secret')
def secret_page():
    # 403 алдаа үүсгэх жишээ
    abort(403)

# ---- ERROR HANDLERS ----
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 ERROR — Page Not Found!</h1>", 404

@app.errorhandler(403)
def forbidden(e):
    return "<h1>403 ERROR — Access Forbidden!</h1>", 403


if __name__ == '__main__':
    app.run(debug=True)
