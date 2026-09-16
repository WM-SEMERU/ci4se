def upcoming_shabbat(self):
    if self.is_shabbat:
        return self
    saturday = self.gdate + datetime.timedelta((12 - self.gdate.weekday()) % 7)
    return HDate(saturday, diaspora=self.diaspora, hebrew=self.hebrew)