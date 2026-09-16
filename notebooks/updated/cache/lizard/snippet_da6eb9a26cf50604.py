def run_send_nologin(*args):
    for user_rec in MUser.query_nologin():
        email_add = user_rec.user_email
        print(email_add)
        send_mail([email_add], '{0}|{1}'.format(SMTP_CFG['name'], email_cfg
            ['title']), email_cfg['content'])
        MUser.set_sendemail_time(user_rec.uid)