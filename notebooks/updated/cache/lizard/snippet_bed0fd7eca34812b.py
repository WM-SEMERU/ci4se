async def send_mail(self, sender, recipients, message, mail_options=None,
    rcpt_options=None):
    return await self.sendmail(sender, recipients, message, mail_options,
        rcpt_options)