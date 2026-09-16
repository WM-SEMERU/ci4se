def score(self, eval_instances, verbosity=0):
    if hasattr(self, '_using_default_combined'
        ) and self._using_default_combined:
        raise NotImplementedError
    self._using_default_separate = True
    return self.predict_and_score(eval_instances, verbosity=verbosity)[1]