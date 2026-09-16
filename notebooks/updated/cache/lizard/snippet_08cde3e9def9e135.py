def show_stack(self, message_regex='^.*$', min_level=logging.DEBUG, limit=
    4096, once=True):
    value = re.compile(message_regex), limit, once, min_level
    self.show_stack_regexes.append(value)