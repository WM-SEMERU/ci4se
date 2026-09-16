def postcode(self):
    return '%03d-%04d' % (self.generator.random.randint(0, 999), self.
        generator.random.randint(0, 9999))