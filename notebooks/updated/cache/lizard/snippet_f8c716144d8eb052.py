def get_feedback(self, feedback=None, **kwargs):
    raise NotImplementedError
    if feedback is not None:
        kwargs['feedback'] = feedback
    kwargs['context'] = 'feedback'
    return self.filter(**kwargs)