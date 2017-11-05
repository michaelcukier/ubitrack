from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import commands

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('upload.html')


@app.errorhandler(500)
def internalServError(error):
    data = "Please make sure all the fields are filled in properly"
    return render_template("upload.html", error=data)


@app.errorhandler(404)
def pageNotFound(error):
    data = "This page doesn't exist, please verify URL"
    return render_template("upload.html", error=data)


@app.errorhandler(503)
def serverOverload(error):
    data = "Server is currently overloaded. Please try again."
    return render_template("upload.html", error=data)


@app.route('/uploader/', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':

        f = request.files['file']

        if secure_filename(f.filename).split(".")[1] != "py":
            data = "error: incorrect correct .py file"
            return render_template("upload.html", warning=data)

        pyversion = request.form.get('pythonversion')

        # download libraries
        getLibraries = request.form['libraries']
        getLibraries = getLibraries.split(",")
        if pyversion == "271":
            for lib in getLibraries:
                result1 = commands.getoutput('sudo wine pip install ' + str(lib))
        elif pyversion == "333":
            for lib in getLibraries:
                result1 = commands.getoutput('sudo wine /root/.wine/drive_c/Python33/Scripts/pip.exe install ' + str(lib))

        # save file in pyInstaller dir
        if pyversion == "271":
            f = request.files['file']
            fullDirFilePyInstaller = '/root/.wine/drive_c/Python27/Scripts/' + secure_filename(f.filename)
            f.save(fullDirFilePyInstaller)
        elif pyversion == "333":
            f = request.files['file']
            fullDirFilePyInstaller = '/root/.wine/drive_c/Python33/Scripts/' + secure_filename(f.filename)
            f.save(fullDirFilePyInstaller)

        # copy the file to ./
        if pyversion == "271":
            result2 = commands.getoutput('echo %s|sudo -S %s' % ("HIDDEN", "cp /root/.wine/drive_c/Python27/Scripts/" + secure_filename(f.filename) + " /"))
        elif pyversion == "333":
            result2 = commands.getoutput('echo %s|sudo -S %s' % ("HIDDEN", "cp /root/.wine/drive_c/Python33/Scripts/" + secure_filename(f.filename) + " /"))

        # execute pyInstaller through Wine
        if pyversion == "271":
            command = "wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile " + secure_filename(f.filename)
            result3 = commands.getoutput('echo %s|sudo -S %s' % ("HIDDEN", command))
        elif pyversion == "333":
            command = "wine /root/.wine/drive_c/Python33/Scripts/pyinstaller.exe --onefile " + secure_filename(f.filename)
            result3 = commands.getoutput('echo %s|sudo -S %s' % ("HIDDEN", command))

        # modify .spec file
        def generateSpecFile(v):
            niceSpec = """
# -*- mode: python -*-
block_cipher = None


a = Analysis(['""" + str(secure_filename(f.filename)) + """'],
             pathex=['Z:\\Python""" + str(v) + """\\Scripts', '~/.wine/drive_c/Python""" + str(v) + """/Lib/site-packages'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='""" + secure_filename(f.filename).split('.')[0] + """"',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )"""
            return niceSpec

        result4 = commands.getoutput('sudo chmod 777 /' + secure_filename(f.filename).split('.')[0] + ".spec")

        if pyversion == "271":
            result5 = commands.getoutput('sudo echo "' + str(generateSpecFile("27")) + '" > ' + secure_filename(f.filename).split('.')[0] + ".spec")
        elif pyversion == "333":
            result5 = commands.getoutput('sudo echo "' + str(generateSpecFile("33")) + '" > ' + secure_filename(f.filename).split('.')[0] + ".spec")

        if pyversion == "271":
            result6 = commands.getoutput('sudo wine pyinstaller.exe ' + secure_filename(f.filename).split('.')[0] + ".spec")
        elif pyversion == "333":
            result6 = commands.getoutput('sudo wine /root/.wine/drive_c/Python33/Scripts/pyinstaller.exe ' + secure_filename(f.filename).split('.')[0] + ".spec")

        result7 = commands.getoutput('cp /dist/' + str(secure_filename(f.filename).split('.')[0]) + ".exe /var/www/py2app/py2app/static/pytoconvert/" + str(secure_filename(f.filename).split('.')[0]) + ".exe")

        data = ["http://www.py2app.pw/static/pytoconvert/" + str(secure_filename(f.filename).split('.')[0]) + ".exe",
                str(secure_filename(f.filename).split('.')[0]) + ".exe"]
        return render_template("upload.html", success=data)


if __name__ == '__main__':
    app.run()
