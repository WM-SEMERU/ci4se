def get_comments(self):
    if self.retrieved:
        raise errors.IllegalState('List has already been retrieved.')
    self.retrieved = True
    return objects.CommentList(self._results, runtime=self._runtime)