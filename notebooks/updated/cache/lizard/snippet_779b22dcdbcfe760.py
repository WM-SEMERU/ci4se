def write_result(self, result):
    assert not self.finished, 'Already sent a response'
    if not self.result.thrift_spec:
        self.finished = True
        return
    spec = self.result.thrift_spec[0]
    if result is not None:
        assert spec, 'Tried to return a result for a void method.'
        setattr(self.result, spec[2], result)
    self.finished = True