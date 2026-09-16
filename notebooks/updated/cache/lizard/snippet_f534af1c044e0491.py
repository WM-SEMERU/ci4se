def create(cls, record, bucket):
    rb = cls(record=record, bucket=bucket)
    db.session.add(rb)
    return rb