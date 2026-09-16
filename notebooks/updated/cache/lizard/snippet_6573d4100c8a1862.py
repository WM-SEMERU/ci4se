def match_star(self, tokens, item):
    head_matches, last_matches = None, None
    if len(tokens) == 1:
        middle = tokens[0]
    elif len(tokens) == 2:
        if isinstance(tokens[0], str):
            middle, last_matches = tokens
        else:
            head_matches, middle = tokens
    else:
        head_matches, middle, last_matches = tokens
    self.add_check('_coconut.isinstance(' + item + ', _coconut.abc.Iterable)')
    if head_matches is None and last_matches is None:
        if middle != wildcard:
            self.add_def(middle + ' = _coconut.list(' + item + ')')
    else:
        itervar = self.get_temp_var()
        self.add_def(itervar + ' = _coconut.list(' + item + ')')
        with self.down_a_level():
            req_length = (len(head_matches) if head_matches is not None else 0
                ) + (len(last_matches) if last_matches is not None else 0)
            self.add_check('_coconut.len(' + itervar + ') >= ' + str(
                req_length))
            if middle != wildcard:
                head_splice = str(len(head_matches)
                    ) if head_matches is not None else ''
                last_splice = '-' + str(len(last_matches)
                    ) if last_matches is not None else ''
                self.add_def(middle + ' = ' + itervar + '[' + head_splice +
                    ':' + last_splice + ']')
            if head_matches is not None:
                self.match_all_in(head_matches, itervar)
            if last_matches is not None:
                for x in range(1, len(last_matches) + 1):
                    self.match(last_matches[-x], itervar + '[-' + str(x) + ']')