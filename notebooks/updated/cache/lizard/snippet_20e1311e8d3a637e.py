def expects_call(self):
    self._callable = ExpectedCall(self, call_name=self._name, callable=True)
    return self