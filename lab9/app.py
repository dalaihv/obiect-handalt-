from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route('/branch')
def branch_list():
    con = sqlite3.connect("lab9.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from tbl_branch")
    b = cur.fetchall()
    return render_template("branch.html", branches = b)
@app.route('/worker')
def worker_list():
  con = sqlite3.connect("lab9.db")
  con.row_factory = sqlite3.Row
  cur = con.cursor()
  cur.execute('''SELECT wid, wname, wowog, bname,bid
        FROM worker w
        INNER JOIN tbl_branch b ON b.bid = w.branch''')
  w = cur.fetchall()
  return render_template("worker.html",workers = w)     

if __name__ == '__main__':
    app.run(debug=True)
