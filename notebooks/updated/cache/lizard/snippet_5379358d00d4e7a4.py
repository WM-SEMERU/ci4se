def store_sent_mail(self, mail):
    if self.sent_box is not None:
        return self.store_mail(self.sent_box, mail)