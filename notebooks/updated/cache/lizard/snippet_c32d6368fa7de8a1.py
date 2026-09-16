def get_result_warn(self, line):
    res = self.RESULT_WARN_SEARCH.search(line)
    try:
        return LogItem(res.group(1), None, None)
    except (AttributeError, IndexError):
        pass
    res = self.RESULT_WARN_SEARCH_CUSTOM.search(line)
    try:
        return LogItem(res.group(1), None, res.group(2))
    except (AttributeError, IndexError):
        return None