def merge_section(self, section, filter_func=None):
    for check in section.checks:
        if filter_func and not filter_func(check):
            continue
        self.add_check(check)