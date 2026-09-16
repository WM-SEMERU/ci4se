def send(self, attachment_failure=False):
    if not self.config['shutit.core.alerting.emailer.send_mail']:
        self.shutit.log('emailer.send: Not configured to send mail!', level
            =logging.INFO)
        return True
    msg = self.__compose()
    mailto = [self.config['shutit.core.alerting.emailer.mailto']]
    smtp = self.__get_smtp()
    if self.config['shutit.core.alerting.emailer.username'] != '':
        smtp.login(self.config['shutit.core.alerting.emailer.username'],
            self.config['shutit.core.alerting.emailer.password'])
    if self.config['shutit.core.alerting.emailer.mailto_maintainer']:
        mailto.append(self.config['shutit.core.alerting.emailer.maintainer'])
    try:
        self.shutit.log('Attempting to send email', level=logging.INFO)
        smtp.sendmail(self.config['shutit.core.alerting.emailer.mailfrom'],
            mailto, msg.as_string())
    except SMTPSenderRefused as refused:
        code = refused.args[0]
        if code == 552 and not attachment_failure:
            self.shutit.log('Mailserver rejected message due to ' +
                'oversize attachments, attempting to resend without', level
                =logging.INFO)
            self.attaches = []
            self.lines.append('Oversized attachments not sent')
            self.send(attachment_failure=True)
        else:
            self.shutit.log('Unhandled SMTP error:' + str(refused), level=
                logging.INFO)
            if not self.config['shutit.core.alerting.emailer.safe_mode']:
                raise refused
    except Exception as error:
        self.shutit.log('Unhandled exception: ' + str(error), level=logging
            .INFO)
        if not self.config['shutit.core.alerting.emailer.safe_mode']:
            raise error
    finally:
        smtp.quit()