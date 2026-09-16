def decorate_callable(self, target):

    def absorb_mocks(test_case, *args):
        return target(test_case)
    should_absorb = not (self.pass_mocks or isinstance(target, type))
    result = absorb_mocks if should_absorb else target
    for patcher in self.patchers:
        result = patcher(result)
    return result