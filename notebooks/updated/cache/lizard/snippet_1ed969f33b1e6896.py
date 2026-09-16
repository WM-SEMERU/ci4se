def increment_qualification_score(self, name, worker_id, notify=False):
    result = self.get_current_qualification_score(name, worker_id)
    current_score = result['score'] or 0
    new_score = current_score + 1
    qtype_id = result['qtype']['id']
    self.assign_qualification(qtype_id, worker_id, new_score, notify)
    return {'qtype': result['qtype'], 'score': new_score}