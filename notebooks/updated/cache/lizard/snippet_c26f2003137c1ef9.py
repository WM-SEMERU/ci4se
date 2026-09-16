def star_assign_item_check(self, original, loc, tokens):
    return self.check_py('3',
        "starred assignment (add 'match' to front to produce universal code)",
        original, loc, tokens)