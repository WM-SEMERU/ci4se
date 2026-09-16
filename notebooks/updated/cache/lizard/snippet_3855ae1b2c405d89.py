def remember_order(self):
    if self._callable:
        raise FakeDeclarationError(
            'remember_order() cannot be used for Fake(callable=True) or Fake(expect_call=True)'
            )
    self._expected_call_order = ExpectedCallOrder(self)
    registry.remember_expected_call_order(self._expected_call_order)
    return self