def get_requirement_warn(self, line):
    res = self.REQ_WARN_SEARCH.search(line)
    try:
        return LogItem(res.group(1), None, None)
    except (AttributeError, IndexError):
        return None