def async_stmt_check(self, original, loc, tokens):
    return self.check_py('35', 'async for/with', original, loc, tokens)