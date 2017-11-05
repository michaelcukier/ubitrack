from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from connectdb import connection
from functools import wraps
from MySQLdb import escape_string as thwart
import gc

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home'))


@app.route("/", subdomain="mobile")
def m():
    return "mobile version"


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return wrap


@app.route('/')
def home():
    c, conn = connection()
    c.execute("SELECT * FROM projects ORDER BY position;")
    data = c.fetchall()
    return render_template('listProjects.html', data=data)


@app.route('/projects/<name>')
def projects(name):
    c, conn = connection()
    data = c.execute("SELECT * FROM projects WHERE alias = '{}'".format(thwart(name)))
    if int(data) == 1:
        data = c.fetchall()
        return render_template("projects.html", data=data)
    else:
        return redirect(url_for('home'))


@app.route("/logout/")
@login_required
def logout():
    session.clear()
    gc.collect()
    return redirect(url_for("home"))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if (request.form['username'] == "michaelcukier") and (request.form['password'] == "Zorro.999"):
            session['logged_in'] = True
            return redirect(url_for('manage'))
        else:
            return render_template("login_page.html")
    else:
        return render_template("login_page.html")


@app.route('/create_post/', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        c, conn = connection()

        # getting all the data from the page
        getImgs = request.form['imgUrls']
        getFullDesc = request.form['fullDesc']
        getTechUsed = request.form['techUsed']
        getTitle = request.form['title']
        getBriefDesc = request.form['briefDesc']
        getHowDoesItWork = request.form['howDoesItWork']
        getAlias = request.form['alias']
        getLink = request.form['link']
        getLinkText = request.form['linkText']
        getPosition = request.form['position']

        c.execute('INSERT INTO projects (imgs, full_desc, tech_used, title, brief_desc, howdoesitwork, alias, link, linkText, position) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (getImgs, getFullDesc, getTechUsed, getTitle, getBriefDesc, getHowDoesItWork, getAlias, getLink, getLinkText, getPosition))
        conn.commit()

        return redirect(url_for('home'))
    else:
        return render_template("create_post.html")


@app.route("/manage/")
@login_required
def manage():
    c, conn = connection()
    c.execute("SELECT * FROM projects ORDER BY position;")
    data = c.fetchall()
    return render_template('manage.html', data=data)


@app.route('/edit_post/<name>', methods=['GET', 'POST'])
@login_required
def edit_post(name):
    c, conn = connection()
    data = c.execute("SELECT * FROM projects WHERE alias = '{}'".format(thwart(name)))
    if int(data) == 1:
        if request.method == "POST":
            # getting all the data from the page
            getImgs = request.form['imgUrls']
            getFullDesc = request.form['fullDesc']
            getTechUsed = request.form['techUsed']
            getTitle = request.form['title']
            getBriefDesc = request.form['briefDesc']
            getHowDoesItWork = request.form['howDoesItWork']
            getAlias = request.form['alias']
            getLink = request.form['link']
            getLinkText = request.form['linkText']
            getPosition = request.form['position']

            if (getFullDesc != "") and (getHowDoesItWork != ""):
                c.execute('UPDATE projects SET '
                          'imgs = (%s), '
                          'full_desc = (%s), '
                          'tech_used = (%s), '
                          'title = (%s), '
                          'brief_desc = (%s), '
                          'howdoesitwork = (%s), '
                          'alias = (%s), '
                          'link = (%s), '
                          'linkText = (%s), '
                          'position = (%s) '
                          'WHERE '
                          'alias = (%s)', (getImgs, getFullDesc, getTechUsed, getTitle, getBriefDesc, getHowDoesItWork, getAlias, getLink, getLinkText, getPosition, getAlias))
                conn.commit()
            else:
                c.execute('UPDATE projects SET '
                          'imgs = (%s), '
                          'tech_used = (%s), '
                          'title = (%s), '
                          'brief_desc = (%s), '
                          'alias = (%s), '
                          'link = (%s), '
                          'linkText = (%s), '
                          'position = (%s) '
                          'WHERE '
                          'alias = (%s)', (getImgs, getTechUsed, getTitle, getBriefDesc, getAlias, getLink, getLinkText, getPosition, getAlias))
                conn.commit()

            return redirect(url_for('manage'))
        else:
            data = c.fetchall()
            return render_template("edit_post.html", data=data)
    else:
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()


