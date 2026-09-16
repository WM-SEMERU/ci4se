def get_assessment_parts(self):
    if self.retrieved:
        raise errors.IllegalState('List has already been retrieved.')
    self.retrieved = True
    return objects.AssessmentPartList(self._results, runtime=self._runtime)