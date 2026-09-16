def stub():
    form = cgi.FieldStorage()
    userid = form['userid'].value
    password = form['passwd'].value
    group = form['group'].value