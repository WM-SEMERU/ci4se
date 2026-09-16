def rosh_hashana_dow(self):
    jdn = conv.hdate_to_jdn(HebrewDate(self.hdate.year, Months.Tishrei, 1))
    return (jdn + 1) % 7 + 1