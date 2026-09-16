def check_len_in(self, min_len, max_len, item):
    if max_len is None:
        if min_len:
            self.add_check('_coconut.len(' + item + ') >= ' + str(min_len))
    elif min_len == max_len:
        self.add_check('_coconut.len(' + item + ') == ' + str(min_len))
    elif not min_len:
        self.add_check('_coconut.len(' + item + ') <= ' + str(max_len))
    else:
        self.add_check(str(min_len) + ' <= _coconut.len(' + item + ') <= ' +
            str(max_len))