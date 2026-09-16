def fmt(self):
    val = str(self.year)
    if self.month is not None:
        val += ' ' + str(self.month)
        if self.day is not None:
            val += ' ' + str(self.day)
    return val