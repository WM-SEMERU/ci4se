def ssn(self, min_age=16, max_age=90):
    age = datetime.timedelta(days=self.generator.random.randrange(min_age *
        365, max_age * 365))
    birthday = datetime.date.today() - age
    if birthday.year < 2000:
        ik = self.generator.random.choice(('3', '4'))
    elif birthday.year < 2100:
        ik = self.generator.random.choice(('5', '6'))
    else:
        ik = self.generator.random.choice(('7', '8'))
    ik += '%02d%02d%02d' % (birthday.year % 100, birthday.month, birthday.day)
    ik += str(self.generator.random.randrange(0, 999)).zfill(3)
    return ik + str(checksum([int(ch) for ch in ik]))