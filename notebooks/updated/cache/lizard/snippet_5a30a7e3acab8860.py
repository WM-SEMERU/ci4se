def message(self, MSG_LEVEL, str):
    caller = get_caller()
    if MSG_LEVEL <= self.verbose:
        print('[{0}.{1}()] {2}'.format(__name__, caller.co_name, str))