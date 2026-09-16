def lastCall(self):
    last_index = len(super(SinonSpy, self)._get_wrapper().call_list) - 1
    return self.getCall(last_index)