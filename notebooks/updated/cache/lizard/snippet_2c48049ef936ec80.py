def await_item_handle(self, original, loc, tokens):
    internal_assert(len(tokens) == 1, 'invalid await statement tokens', tokens)
    if not self.target:
        self.make_err(CoconutTargetError,
            'await requires a specific target', original, loc, target='sys')
    elif self.target_info >= (3, 5):
        return 'await ' + tokens[0]
    elif self.target_info >= (3, 3):
        return '(yield from ' + tokens[0] + ')'
    else:
        return '(yield _coconut.asyncio.From(' + tokens[0] + '))'