def send_mail(to_addr, subj_msg, body_msg, attach_path, serv_addr,
    serv_port, from_addr, passwd):
    msg = MIMEMultipart()
    if attach_path is not None:
        with open(attach_path, 'rb') as fin:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(fin.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                'attachment; filename={0}'.format(attach_path))
            msg.attach(part)
    else:
        pass
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subj_msg
    msg.attach(MIMEText(body_msg, 'plain'))
    server = smtplib.SMTP(serv_addr, serv_port)
    server.starttls()
    server.login(from_addr, passwd)
    text_msg = msg.as_string()
    server.sendmail(from_addr, to_addr, text_msg)
    server.quit