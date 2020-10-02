from core import app

from flask import render_template

@app.route('/startpage')
def startpage():

    return render_template('startpage.html')