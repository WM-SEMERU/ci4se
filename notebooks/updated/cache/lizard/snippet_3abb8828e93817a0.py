def GMailer(recipients, username, password, subject='Log message from lggr.py'
    ):
    import smtplib
    srvr = smtplib.SMTP('smtp.gmail.com', 587)
    srvr.ehlo()
    srvr.starttls()
    srvr.ehlo()
    srvr.login(username, password)
    if not (isinstance(recipients, list) or isinstance(recipients, tuple)):
        recipients = [recipients]
    gmail_sender = '{0}@gmail.com'.format(username)
    msg = 'To: {0}\nFrom: ' + gmail_sender + '\nSubject: ' + subject + '\n'
    msg = msg + '\n{1}\n\n'
    try:
        while True:
            logstr = yield
            for rcp in recipients:
                message = msg.format(rcp, logstr)
                srvr.sendmail(gmail_sender, rcp, message)
    except GeneratorExit:
        srvr.quit()