from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from werkzeug.utils import secure_filename
from functools import wraps
import gc
import MySQLdb

app = Flask(__name__)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('admin'))
    return wrap


def connectDB():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="cukier", db="pythonprogramming")
    c = conn.cursor()
    conn.set_character_set('utf8')
    c.execute('SET NAMES utf8;')
    c.execute('SET CHARACTER SET utf8;')
    c.execute('SET character_set_connection=utf8;')
    return conn, c


@app.route("/logout/")
@login_required
def logout():
    session.clear()
    gc.collect()
    return redirect(url_for("homepage"))


@app.route('/')
def homepage():
    conn, c = connectDB()

    c.execute('SELECT * FROM lux_members WHERE honor="standard"')
    list_membres_standard = c.fetchall()

    c.execute('SELECT * FROM lux_members WHERE honor="honored"')
    list_membres_honored = c.fetchall()

    c.execute('SELECT * FROM lux_pub')
    list_pub = c.fetchall()

    c.execute('SELECT * FROM lux_content WHERE whichPage="homepage";')
    content_homepage = c.fetchone()[2].decode("utf8")

    return render_template('index.html', list_membres_standard=list_membres_standard, list_membres_honored=list_membres_honored, list_pub=list_pub, content_homepage=content_homepage)


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/decouvrir/')
def decouvrir():
    return render_template('decouvrir.html')


@app.route('/events/')
def events():
    conn, c = connectDB()

    c.execute('SELECT * FROM lux_events')
    result = c.fetchall()

    return render_template('event.html', result=result)


@app.route('/credits/')
def credits():
    return render_template('credits.html')


@app.route('/investir/')
def investir():
    return render_template('investir.html')


@app.route('/membres/')
def membres():
    conn, c = connectDB()

    c.execute('SELECT * FROM lux_members')
    result = c.fetchall()

    return render_template('membres.html', result=result)


@app.route('/mentions/')
def mentions():
    return render_template('mentions.html')


@app.route('/shopping/')
def shopping():
    return render_template('shopping.html')


@app.route('/login/', methods=['GET', 'POST'])
def admin():
    if request.method == "POST":
        if (request.form['username'] == "admin") and (request.form['password'] == "admin"):
            session['logged_in'] = True
            return redirect(url_for('dashBoardAdmin'))
        elif (request.form['username'] == "cdl") and (request.form['password'] == "cdl"):
            session['logged_in'] = True
            return redirect(url_for('cdlDash'))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route('/admin/dash/')
@login_required
def dashBoardAdmin():
    return render_template("accesadmin/dashboard.html")


@app.route('/admin/publications/', methods=['GET', 'POST'])
@login_required
def admin_publications():
    if request.method == 'POST':
        if "formMembers" in request.form :
            conn, c = connectDB()

            member_name = request.form['member_name']
            member_surname = request.form['member_surname']
            member_status = request.form['member_status']
            member_etoiles = request.form['member_etoiles']
            member_adresse = request.form['member_adresse']
            member_honor = request.form.get('member_honor')

            f = request.files['file']
            fullDirFile = '/var/www/dev_lux/dev_lux/static/uploaded_pics/' + secure_filename(f.filename)
            f.save(fullDirFile)

            c.execute(
                'INSERT INTO lux_members (member_name, member_surname, member_status, member_etoiles, member_addr, member_img, honor) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                (str(member_name), str(member_surname), str(member_status), str(member_etoiles), str(member_adresse),
                 str(secure_filename(f.filename)), str(member_honor)))
            conn.commit()

            success = "membre poste"
            return render_template('accesadmin/publications.html', success=success)

        elif "formEvents" in request.form:
            conn, c = connectDB()

            f = request.files['file']
            fullDirFile = '/var/www/dev_lux/dev_lux/static/uploaded_pics/' + secure_filename(f.filename)
            f.save(fullDirFile)

            event_description = request.form['event_description']
            event_date = request.form['event_date']

            c.execute("INSERT INTO lux_events (event_date, event_description, event_image) VALUES (%s, %s, %s)", (str(event_date), str(event_description), str(secure_filename(f.filename))))
            conn.commit()

            success = "actu postee"
            return render_template('accesadmin/publications.html', success=success)

        elif "formAnnonce" in request.form:
            conn, c = connectDB()

            f = request.files['file1']
            fullDirFile = '/var/www/dev_lux/dev_lux/static/uploaded_pics/' + secure_filename(f.filename)
            f.save(fullDirFile)

            contenu = request.form['contenu']
            titre_publication = request.form['titre_publication']

            c.execute("INSERT INTO lux_annonces (titre, contenu, image) VALUES (%s, %s, %s)", (str(contenu), str(titre_publication), str(secure_filename(f.filename))))
            conn.commit()

            success = "annonce postee"
            return render_template('accesadmin/publications.html', success=success)
    else:
        return render_template("accesadmin/publications.html")


@app.route('/admin/langues/', methods=['GET', 'POST'])
@login_required
def admin_langues():
    if request.method == 'POST':
        if "form_trad_membres" in request.form:

            conn, c = connectDB()

            txt_fr_1 = request.form['trad-fr-1']
            txt_fr_2 = request.form['trad-fr-2']
            txt_fr_3 = request.form['trad-fr-3']
            txt_fr_4 = request.form['trad-fr-4']
            txt_fr_5 = request.form['trad-fr-5']
            txt_fr_6 = request.form['trad-fr-6']
            txt_fr_7 = request.form['trad-fr-7']
            txt_fr_8 = request.form['trad-fr-8']
            txt_fr_9 = request.form['trad-fr-9']

            txt_en_1 = request.form['trad-en-1']
            txt_en_2 = request.form['trad-en-2']
            txt_en_3 = request.form['trad-en-3']
            txt_en_4 = request.form['trad-en-4']
            txt_en_5 = request.form['trad-en-5']
            txt_en_6 = request.form['trad-en-6']
            txt_en_7 = request.form['trad-en-7']
            txt_en_8 = request.form['trad-en-8']
            txt_en_9 = request.form['trad-en-9']

            txt_lux_1 = request.form['trad-lux-1']
            txt_lux_2 = request.form['trad-lux-2']
            txt_lux_3 = request.form['trad-lux-3']
            txt_lux_4 = request.form['trad-lux-4']
            txt_lux_5 = request.form['trad-lux-5']
            txt_lux_6 = request.form['trad-lux-6']
            txt_lux_7 = request.form['trad-lux-7']
            txt_lux_8 = request.form['trad-lux-8']
            txt_lux_9 = request.form['trad-lux-9']

            txt_all_1 = request.form['trad-all-1']
            txt_all_2 = request.form['trad-all-2']
            txt_all_3 = request.form['trad-all-3']
            txt_all_4 = request.form['trad-all-4']
            txt_all_5 = request.form['trad-all-5']
            txt_all_6 = request.form['trad-all-6']
            txt_all_7 = request.form['trad-all-7']
            txt_all_8 = request.form['trad-all-8']
            txt_all_9 = request.form['trad-all-9']

            c.execute('UPDATE lux_content SET txt_fr_1 = %s, txt_fr_2 = %s, txt_fr_3 = %s, txt_fr_4 = %s, txt_fr_5 = %s, txt_fr_6 = %s, txt_fr_7 = %s, txt_fr_8 = %s, txt_fr_9 = %s WHERE page="members"', (txt_fr_1, txt_fr_2, txt_fr_3, txt_fr_4, txt_fr_5, txt_fr_6, txt_fr_7, txt_fr_8, txt_fr_9))
            conn.commit()

            c.execute('UPDATE lux_content SET txt_en_1 = %s, txt_en_2 = %s, txt_en_3 = %s, txt_en_4 = %s, txt_en_5 = %s, txt_en_6 = %s, txt_en_7 = %s, txt_en_8 = %s, txt_en_9 = %s WHERE page="members"', (txt_en_1, txt_en_2, txt_en_3, txt_en_4, txt_en_5, txt_en_6, txt_en_7, txt_en_8, txt_en_9))
            conn.commit()

            c.execute('UPDATE lux_content SET txt_lux_1 = %s, txt_lux_2 = %s, txt_lux_3 = %s, txt_lux_4 = %s, txt_lux_5 = %s, txt_lux_6 = %s, txt_lux_7 = %s, txt_lux_8 = %s, txt_lux_9 = %s WHERE page="members"', (txt_lux_1, txt_lux_2, txt_lux_3, txt_lux_4, txt_lux_5, txt_lux_6, txt_lux_7, txt_lux_8, txt_lux_9))
            conn.commit()

            c.execute('UPDATE lux_content SET txt_all_1 = %s, txt_all_2 = %s, txt_all_3 = %s, txt_all_4 = %s, txt_all_5 = %s, txt_all_6 = %s, txt_all_7 = %s, txt_all_8 = %s, txt_all_9 = %s WHERE page="members"', (txt_all_1, txt_all_2, txt_all_3, txt_all_4, txt_all_5, txt_all_6, txt_all_7, txt_all_8, txt_all_9))
            conn.commit()

            return redirect(url_for('admin_langues'))

        elif "form_investir" in request.form:

            conn, c = connectDB()

            txt_fr_1 = request.form['trad-fr-1-1']
            txt_fr_2 = request.form['trad-fr-2-2']
            txt_fr_3 = request.form['trad-fr-3-3']
            txt_fr_4 = request.form['trad-fr-4-4']
            txt_fr_5 = request.form['trad-fr-5-5']

            txt_en_1 = request.form['trad-en-1-1']
            txt_en_2 = request.form['trad-en-2-2']
            txt_en_3 = request.form['trad-en-3-3']
            txt_en_4 = request.form['trad-en-4-4']
            txt_en_5 = request.form['trad-en-5-5']

            txt_lux_1 = request.form['trad-lux-1-1']
            txt_lux_2 = request.form['trad-lux-2-2']
            txt_lux_3 = request.form['trad-lux-3-3']
            txt_lux_4 = request.form['trad-lux-4-4']
            txt_lux_5 = request.form['trad-lux-5-5']

            txt_all_1 = request.form['trad-all-1-1']
            txt_all_2 = request.form['trad-all-2-2']
            txt_all_3 = request.form['trad-all-3-3']
            txt_all_4 = request.form['trad-all-4-4']
            txt_all_5 = request.form['trad-all-5-5']


            c.execute('UPDATE lux_content SET txt_fr_1 = %s, txt_fr_2 = %s, txt_fr_3 = %s, txt_fr_4 = %s, txt_fr_5 = %s WHERE page="investir"', (txt_fr_1, txt_fr_2, txt_fr_3, txt_fr_4, txt_fr_5))
            conn.commit()

            c.execute('UPDATE lux_content SET txt_en_1 = %s, txt_en_2 = %s, txt_en_3 = %s, txt_en_4 = %s, txt_en_5 = %s WHERE page="investir"', (txt_en_1, txt_en_2, txt_en_3, txt_en_4, txt_en_5))
            conn.commit()

            c.execute('UPDATE lux_content SET txt_lux_1 = %s, txt_lux_2 = %s, txt_lux_3 = %s, txt_lux_4 = %s, txt_lux_5 = %s WHERE page="investir"', (txt_lux_1, txt_lux_2, txt_lux_3, txt_lux_4, txt_lux_5))
            conn.commit()

            c.execute('UPDATE lux_content SET txt_all_1 = %s, txt_all_2 = %s, txt_all_3 = %s, txt_all_4 = %s, txt_all_5 = %s WHERE page="investir"', (txt_all_1, txt_all_2, txt_all_3, txt_all_4, txt_all_5))
            conn.commit()

            return redirect(url_for('admin_langues'))

        elif "form_decouvrir" in request.form:
            conn, c = connectDB()

            txt_fr_1 = request.form['trad-fr-d1']
            txt_fr_2 = request.form['trad-fr-d2']
            txt_fr_3 = request.form['trad-fr-d3']
            txt_fr_4 = request.form['trad-fr-d4']

            txt_en_1 = request.form['trad-en-d1']
            txt_en_2 = request.form['trad-en-d2']
            txt_en_3 = request.form['trad-en-d3']
            txt_en_4 = request.form['trad-en-d4']

            txt_lux_1 = request.form['trad-lux-d1']
            txt_lux_2 = request.form['trad-lux-d2']
            txt_lux_3 = request.form['trad-lux-d3']
            txt_lux_4 = request.form['trad-lux-d4']

            txt_all_1 = request.form['trad-all-d1']
            txt_all_2 = request.form['trad-all-d2']
            txt_all_3 = request.form['trad-all-d3']
            txt_all_4 = request.form['trad-all-d4']

            c.execute('UPDATE lux_content SET txt_fr_1 = %s, txt_fr_2 = %s, txt_fr_3 = %s, txt_fr_4 = %s WHERE page="decouvrir"', (txt_fr_1, txt_fr_2, txt_fr_3, txt_fr_4))
            conn.commit()

            c.execute('UPDATE lux_content SET txt_en_1 = %s, txt_en_2 = %s, txt_en_3 = %s, txt_en_4 = %s WHERE page="decouvrir"', (txt_en_1, txt_en_2, txt_en_3, txt_en_4))
            conn.commit()

            c.execute('UPDATE lux_content SET txt_lux_1 = %s, txt_lux_2 = %s, txt_lux_3 = %s, txt_lux_4 = %s WHERE page="decouvrir"', (txt_lux_1, txt_lux_2, txt_lux_3, txt_lux_4))
            conn.commit()

            c.execute('UPDATE lux_content SET txt_all_1 = %s, txt_all_2 = %s, txt_all_3 = %s, txt_all_4 = %s WHERE page="decouvrir"', (txt_all_1, txt_all_2, txt_all_3, txt_all_4))
            conn.commit()

            return redirect(url_for('admin_langues'))

        elif "form_shopping" in request.form:
            conn, c = connectDB()

            txt_fr_1 = request.form['trad-fr-s1']
            txt_fr_2 = request.form['trad-fr-s2']
            txt_fr_3 = request.form['trad-fr-s3']
            txt_fr_4 = request.form['trad-fr-s4']
            txt_fr_5 = request.form['trad-fr-s5']

            txt_en_1 = request.form['trad-en-s1']
            txt_en_2 = request.form['trad-en-s2']
            txt_en_3 = request.form['trad-en-s3']
            txt_en_4 = request.form['trad-en-s4']
            txt_en_5 = request.form['trad-en-s5']

            txt_lux_1 = request.form['trad-lux-s1']
            txt_lux_2 = request.form['trad-lux-s2']
            txt_lux_3 = request.form['trad-lux-s3']
            txt_lux_4 = request.form['trad-lux-s4']
            txt_lux_5 = request.form['trad-lux-s5']

            txt_all_1 = request.form['trad-all-s1']
            txt_all_2 = request.form['trad-all-s2']
            txt_all_3 = request.form['trad-all-s3']
            txt_all_4 = request.form['trad-all-s4']
            txt_all_5 = request.form['trad-all-s5']


            c.execute('UPDATE lux_content SET txt_fr_1 = %s, txt_fr_2 = %s, txt_fr_3 = %s, txt_fr_4 = %s, txt_fr_5 = %s WHERE page="shopping"', (txt_fr_1, txt_fr_2, txt_fr_3, txt_fr_4, txt_fr_5))
            conn.commit()

            c.execute('UPDATE lux_content SET txt_en_1 = %s, txt_en_2 = %s, txt_en_3 = %s, txt_en_4 = %s, txt_en_5 = %s WHERE page="shopping"', (txt_en_1, txt_en_2, txt_en_3, txt_en_4, txt_en_5))
            conn.commit()

            c.execute('UPDATE lux_content SET txt_lux_1 = %s, txt_lux_2 = %s, txt_lux_3 = %s, txt_lux_4 = %s, txt_lux_5 = %s WHERE page="shopping"', (txt_lux_1, txt_lux_2, txt_lux_3, txt_lux_4, txt_lux_5))
            conn.commit()

            c.execute('UPDATE lux_content SET txt_all_1 = %s, txt_all_2 = %s, txt_all_3 = %s, txt_all_4 = %s, txt_all_5 = %s WHERE page="shopping"', (txt_all_1, txt_all_2, txt_all_3, txt_all_4, txt_all_5))
            conn.commit()

            return redirect(url_for('admin_langues'))

        elif "form_homepage" in request.form:
            conn, c = connectDB()

            hp_fr = request.form['trad-fr-h1']
            hp_en = request.form['trad-en-h2']
            hp_lux = request.form['trad-lux-h3']
            hp_all = request.form['trad-all-h4']

            c.execute('UPDATE lux_content SET txt_fr_1 = %s, txt_en_1 = %s, txt_lux_1 = %s, txt_all_1 = %s WHERE page="homepage"', (hp_fr, hp_en, hp_lux, hp_all))
            conn.commit()

            return redirect(url_for('admin_langues'))


    else:
        conn, c = connectDB()

        c.execute("SELECT * FROM lux_content WHERE page = 'members'")
        txt = c.fetchall()[0]

        txt_fr_1 = txt[1].decode("utf8")
        txt_fr_2 = txt[2].decode("utf8")
        txt_fr_3 = txt[3].decode("utf8")
        txt_fr_4 = txt[4].decode("utf8")
        txt_fr_5 = txt[5].decode("utf8")
        txt_fr_6 = txt[6].decode("utf8")
        txt_fr_7 = txt[7].decode("utf8")
        txt_fr_8 = txt[8].decode("utf8")
        txt_fr_9 = txt[9].decode("utf8")

        txt_en_1 = txt[10].decode("utf8")
        txt_en_2 = txt[11].decode("utf8")
        txt_en_3 = txt[12].decode("utf8")
        txt_en_4 = txt[13].decode("utf8")
        txt_en_5 = txt[14].decode("utf8")
        txt_en_6 = txt[15].decode("utf8")
        txt_en_7 = txt[16].decode("utf8")
        txt_en_8 = txt[17].decode("utf8")
        txt_en_9 = txt[18].decode("utf8")

        txt_lux_1 = txt[19].decode("utf8")
        txt_lux_2 = txt[20].decode("utf8")
        txt_lux_3 = txt[21].decode("utf8")
        txt_lux_4 = txt[22].decode("utf8")
        txt_lux_5 = txt[23].decode("utf8")
        txt_lux_6 = txt[24].decode("utf8")
        txt_lux_7 = txt[25].decode("utf8")
        txt_lux_8 = txt[26].decode("utf8")
        txt_lux_9 = txt[27].decode("utf8")

        txt_all_1 = txt[28].decode("utf8")
        txt_all_2 = txt[29].decode("utf8")
        txt_all_3 = txt[30].decode("utf8")
        txt_all_4 = txt[31].decode("utf8")
        txt_all_5 = txt[32].decode("utf8")
        txt_all_6 = txt[33].decode("utf8")
        txt_all_7 = txt[34].decode("utf8")
        txt_all_8 = txt[35].decode("utf8")
        txt_all_9 = txt[36].decode("utf8")


        c.execute("SELECT * FROM lux_content WHERE page = 'investir'")
        txt2 = c.fetchall()[0]

        line1_invest_fr = txt2[1].decode("utf8")
        line2_invest_fr = txt2[2].decode("utf8")
        line3_invest_fr = txt2[3].decode("utf8")
        line4_invest_fr = txt2[4].decode("utf8")
        line5_invest_fr = txt2[5].decode("utf8")

        line1_invest_en = txt2[10].decode("utf8")
        line2_invest_en = txt2[11].decode("utf8")
        line3_invest_en = txt2[12].decode("utf8")
        line4_invest_en = txt2[13].decode("utf8")
        line5_invest_en = txt2[14].decode("utf8")

        line1_invest_lux = txt2[19].decode("utf8")
        line2_invest_lux = txt2[20].decode("utf8")
        line3_invest_lux = txt2[21].decode("utf8")
        line4_invest_lux = txt2[22].decode("utf8")
        line5_invest_lux = txt2[23].decode("utf8")

        line1_invest_all = txt2[28].decode("utf8")
        line2_invest_all = txt2[29].decode("utf8")
        line3_invest_all = txt2[30].decode("utf8")
        line4_invest_all = txt2[31].decode("utf8")
        line5_invest_all = txt2[32].decode("utf8")


        c.execute("SELECT * FROM lux_content WHERE page = 'decouvrir'")
        txt3 = c.fetchall()[0]

        line1_decouv_fr = txt3[1].decode("utf8")
        line2_decouv_fr = txt3[2].decode("utf8")
        line3_decouv_fr = txt3[3].decode("utf8")
        line4_decouv_fr = txt3[4].decode("utf8")

        line1_decouv_en = txt3[10].decode("utf8")
        line2_decouv_en = txt3[11].decode("utf8")
        line3_decouv_en = txt3[12].decode("utf8")
        line4_decouv_en = txt3[13].decode("utf8")

        line1_decouv_lux = txt3[19].decode("utf8")
        line2_decouv_lux = txt3[20].decode("utf8")
        line3_decouv_lux = txt3[21].decode("utf8")
        line4_decouv_lux = txt3[22].decode("utf8")

        line1_decouv_all = txt3[28].decode("utf8")
        line2_decouv_all = txt3[29].decode("utf8")
        line3_decouv_all = txt3[30].decode("utf8")
        line4_decouv_all = txt3[31].decode("utf8")


        c.execute("SELECT * FROM lux_content WHERE page = 'shopping'")
        txt4 = c.fetchall()[0]

        line1_shop_fr = txt4[1].decode("utf8")
        line2_shop_fr = txt4[2].decode("utf8")
        line3_shop_fr = txt4[3].decode("utf8")
        line4_shop_fr = txt4[4].decode("utf8")
        line5_shop_fr = txt4[5].decode("utf8")

        line1_shop_en = txt4[10].decode("utf8")
        line2_shop_en = txt4[11].decode("utf8")
        line3_shop_en = txt4[12].decode("utf8")
        line4_shop_en = txt4[13].decode("utf8")
        line5_shop_en = txt4[14].decode("utf8")

        line1_shop_lux = txt4[19].decode("utf8")
        line2_shop_lux = txt4[20].decode("utf8")
        line3_shop_lux = txt4[21].decode("utf8")
        line4_shop_lux = txt4[22].decode("utf8")
        line5_shop_lux = txt4[23].decode("utf8")

        line1_shop_all = txt4[28].decode("utf8")
        line2_shop_all = txt4[29].decode("utf8")
        line3_shop_all = txt4[30].decode("utf8")
        line4_shop_all = txt4[31].decode("utf8")
        line5_shop_all = txt4[32].decode("utf8")


        c.execute("SELECT * FROM lux_content WHERE page = 'homepage'")
        txt5 = c.fetchall()[0]
        
        content_homepage_fr = txt4[1].decode("utf8")
        content_homepage_en = txt4[10].decode("utf8")
        content_homepage_lux = txt4[19].decode("utf8")
        content_homepage_all = txt4[28].decode("utf8")

        return render_template("accesadmin/langues.html", **locals())


@app.route('/admin/publicite/', methods=['GET', 'POST'])
@login_required
def admin_pub():
    if request.method == 'POST':  # event
        conn, c = connectDB()

        category = request.form.get('typedepub')
        contenu = request.form['pub_contenu']
        url = request.form['pub_url']

        f = request.files['file']
        fullDirFile = '/var/www/dev_lux/dev_lux/static/uploaded_pics/' + secure_filename(f.filename)
        f.save(fullDirFile)

        c.execute('INSERT INTO lux_pub (category, contenu, image, url) VALUES (%s, %s, %s, %s)',
                  (str(category), str(contenu), str(secure_filename(f.filename)), str(url)))
        conn.commit()

        # bannieres
        c.execute('SELECT * FROM lux_pub WHERE category = "Banniere";')
        bannieres = c.fetchall()

        # bloc loisirs
        c.execute('SELECT * FROM lux_pub WHERE category = "Loisir";')
        loisirs = c.fetchall()

        success = "Publicite rajoutee"

        return render_template("accesadmin/publicites.html", bannieres=bannieres, loisirs=loisirs, success=success)

    else:
        conn, c = connectDB()

        # bannieres
        c.execute('SELECT * FROM lux_pub WHERE category = "Banniere";')
        bannieres = c.fetchall()

        # bloc loisirs
        c.execute('SELECT * FROM lux_pub WHERE category = "Loisir";')
        loisirs = c.fetchall()

        return render_template("accesadmin/publicites.html", bannieres=bannieres, loisirs=loisirs)


@app.route('/deletePub/<indexToDel>')
@login_required
def deletePub(indexToDel):
    conn, c = connectDB()

    c.execute('DELETE FROM lux_pub WHERE id = "' + str(indexToDel) + '";')
    conn.commit()

    # bannieres
    c.execute('SELECT * FROM lux_pub WHERE category = "Banniere";')
    bannieres = c.fetchall()

    # bloc loisirs
    c.execute('SELECT * FROM lux_pub WHERE category = "Loisir";')
    loisirs = c.fetchall()

    success = "Publicitee supprimee"
    return render_template("accesadmin/publicites.html", success=success, bannieres=bannieres, loisirs=loisirs)


@app.route('/cdldash/')
@login_required
def cdlDash():
    return render_template("accescdl/dashboard.html")


if __name__ == "__main__":
    app.run()
