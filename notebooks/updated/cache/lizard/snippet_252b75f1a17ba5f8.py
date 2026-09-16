def valid(self):
    if self.end is None:
        if self.start is not None:
            return self.start <= datetime.datetime.utcnow()
        else:
            return True
    elif self.start is not None:
        return self.start <= datetime.datetime.utcnow() <= self.end
    else:
        return datetime.datetime.utcnow() <= self.end