def _parse_lists(self, match):
    if match.group(4) is None:
        return match.group(0)
    pre, at_char, user, list_name = match.groups()
    list_name = list_name[1:]
    if self._include_spans:
        self._lists.append((user, list_name, match.span(0)))
    else:
        self._lists.append((user, list_name))
    if self._html:
        return '%s%s' % (pre, self.format_list(at_char, user, list_name))