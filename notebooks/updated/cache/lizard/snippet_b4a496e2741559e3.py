def json_data(self):
    return {'type': self.type, 'recruiter': self.recruiter_id,
        'assignment_id': self.assignment_id, 'hit_id': self.hit_id, 'mode':
        self.mode, 'end_time': self.end_time, 'base_pay': self.base_pay,
        'bonus': self.bonus, 'status': self.status}