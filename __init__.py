from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import MySQLdb

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('homepage'))


@app.errorhandler(500)
def page_not_found(e):
    return "The server is currently overloaded. Please try to refresh the page."


@app.route('/')
def homepage():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="cukier", db="pythonprogramming")
    c = conn.cursor()

    conn.set_character_set('utf8')
    c.execute('SET NAMES utf8;')
    c.execute('SET CHARACTER SET utf8;')
    c.execute('SET character_set_connection=utf8;')

    c.execute("SELECT * from articles WHERE mainImage != 'no image' ORDER BY id DESC LIMIT 19;")
    result = c.fetchall()

    # mainImage
    mainImage = [result[0][0].decode("utf8"), result[0][1], result[0][7], result[0][5], result[0][4], result[0][10].decode("utf8")]

    # 4 images top right
    imagesTopRight_topleft = [result[1][0].decode("utf8"), result[1][1], result[1][7], result[1][5], result[1][4], result[1][10].decode("utf8")]
    imagesTopRight_topright = [result[2][0].decode("utf8"), result[2][1], result[2][7], result[2][5], result[2][4], result[2][10].decode("utf8")]
    imagesTopRight_bottomleft = [result[3][0].decode("utf8"), result[3][1], result[3][7], result[3][5], result[3][4], result[3][10].decode("utf8")]
    imagesTopRight_bottomright = [result[4][0].decode("utf8"), result[4][1], result[4][7], result[4][5], result[4][4], result[4][10].decode("utf8")]

    # 9 images middle right
    middleImage1 = [result[5][0].decode("utf8"), result[5][7], result[5][1], result[5][4]]
    middleImage2 = [result[6][0].decode("utf8"), result[6][7], result[6][1], result[6][4]]
    middleImage3 = [result[7][0].decode("utf8"), result[7][7], result[7][1], result[7][4]]
    middleImage4 = [result[8][0].decode("utf8"), result[8][7], result[8][1], result[8][4]]
    middleImage5 = [result[9][0].decode("utf8"), result[9][7], result[9][1], result[9][4]]
    middleImage6 = [result[10][0].decode("utf8"), result[10][7], result[10][1], result[10][4]]
    middleImage7 = [result[11][0].decode("utf8"), result[11][7], result[11][1], result[11][4]]
    middleImage8 = [result[12][0].decode("utf8"), result[12][7], result[12][1], result[12][4]]
    middleImage9 = [result[13][0].decode("utf8"), result[13][7], result[13][1], result[13][4]]

    # 5 more stories
    moreStories1 = [result[14][0].decode("utf8"), result[14][7], result[14][1], result[14][5], result[14][10].decode("utf8"), result[14][5], result[14][4]]
    moreStories2 = [result[15][0].decode("utf8"), result[15][7], result[15][1], result[15][5], result[15][10].decode("utf8"), result[15][5], result[15][4]]
    moreStories3 = [result[16][0].decode("utf8"), result[16][7], result[16][1], result[16][5], result[16][10].decode("utf8"), result[16][5], result[16][4]]
    moreStories4 = [result[17][0].decode("utf8"), result[17][7], result[17][1], result[17][5], result[17][10].decode("utf8"), result[17][5], result[17][4]]
    moreStories5 = [result[18][0].decode("utf8"), result[18][7], result[18][1], result[18][5], result[18][10].decode("utf8"), result[18][5], result[18][4]]

    # 8 latest middle
    c.execute("SELECT * from articles WHERE mainImage = 'no image' ORDER BY id DESC LIMIT 8;")
    result = c.fetchall()

    latest1 = [result[0][0].decode("utf8"), result[0][1], result[0][4], result[0][5]]
    latest2 = [result[1][0].decode("utf8"), result[1][1], result[1][4], result[1][5]]
    latest3 = [result[2][0].decode("utf8"), result[2][1], result[2][4], result[2][5]]
    latest4 = [result[3][0].decode("utf8"), result[3][1], result[3][4], result[3][5]]
    latest5 = [result[4][0].decode("utf8"), result[4][1], result[4][4], result[4][5]]
    latest6 = [result[5][0].decode("utf8"), result[5][1], result[5][4], result[5][5]]
    latest7 = [result[6][0].decode("utf8"), result[6][1], result[6][4], result[6][5]]
    latest8 = [result[7][0].decode("utf8"), result[7][1], result[7][4], result[7][5]]

    # last updated
    c.execute("SELECT * from articles ORDER BY id DESC LIMIT 1;")
    result = c.fetchall()
    lastUpdated = result[0][5]

    return render_template('index.html', **locals())


@app.route('/archives/')
def archives():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="cukier", db="pythonprogramming")
    c = conn.cursor()

    conn.set_character_set('utf8')
    c.execute('SET NAMES utf8;')
    c.execute('SET CHARACTER SET utf8;')
    c.execute('SET character_set_connection=utf8;')

    c.execute("SELECT * from articles ORDER BY id DESC")
    allArticles = c.fetchall()

    allArticles = list(allArticles)

    for art in range(0, len(allArticles)):
        allArticles[art] = list(allArticles[art])

    for elem in range (0, len(allArticles)):
        for e in range(0, len(allArticles[elem])):
            try:
                if (allArticles[elem][e] == "no title (twitter)") or (allArticles[elem][e] == None):
                    allArticles[elem][e] = ""
                else:
                    allArticles[elem][e] = allArticles[elem][e].decode("utf8")
            except AttributeError:
                pass

    return render_template('archives.html', allArticles=allArticles)


if __name__ == "__main__":
    app.run()
