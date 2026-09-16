def add_answer_at_time(self, record, now):
    if record is not None:
        if now == 0 or not record.is_expired(now):
            self.answers.append((record, now))
            if record.rrsig is not None:
                self.answers.append((record.rrsig, now))