def _is_accepted_input(self, input_string):
    ret = False
    accept_filter = self.volume_string, 'http stream debug: '
    reject_filter = ()
    for n in accept_filter:
        if n in input_string:
            ret = True
            break
    if ret:
        for n in reject_filter:
            if n in input_string:
                ret = False
                break
    return ret