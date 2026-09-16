def delete(self, session, commit=True, soft=True):
    if soft:
        self.time_removed = sqlalchemy.func.unix_timestamp()
    else:
        session.delete(self)
    if commit:
        session.commit()