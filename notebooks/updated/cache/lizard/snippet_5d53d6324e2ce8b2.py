def get_event_question(self, id, question_id, **data):
    return self.get('/events/{0}/questions/{0}/'.format(id, question_id),
        data=data)