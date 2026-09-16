def subjects(self):
    for sms in SetMemberSubject.where(subject_set_id=self.id):
        yield sms.links.subject