def timezone(self):
    date = self.message.get('date')
    timezone = 0
    try:
        _, timezone = convert_mail_date(date)
    finally:
        return timezone