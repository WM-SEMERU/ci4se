def parse(self):
    self.tokenize()
    if self.debug:
        print('Tokens found: %s' % self.token_list)
    try:
        parse_tree = self.parse2()
    except Exception as e:
        raise e
    return parse_tree