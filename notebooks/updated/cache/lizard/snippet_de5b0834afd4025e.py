def appendleft(self, value):

    def appendleft_trans(pipe):
        self._appendleft_helper(value, pipe)
    self._transaction(appendleft_trans)