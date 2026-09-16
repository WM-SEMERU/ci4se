def build_date(self):
    if len(self.dutinformation) > 0 and self.dutinformation.get(0
        ).build is not None:
        return self.dutinformation.get(0).build.date
    return None