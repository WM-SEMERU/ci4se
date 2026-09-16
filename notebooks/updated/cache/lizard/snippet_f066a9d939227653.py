def as_dict(self):
    return {'@module': self.__class__.__module__, '@class': self.__class__.
        __name__, 'additional_condition': self._additional_condition,
        'max_nabundant': self.max_nabundant, 'target_environments': self.
        target_environments, 'target_penalty_type': self.
        target_penalty_type, 'max_csm': self.max_csm}