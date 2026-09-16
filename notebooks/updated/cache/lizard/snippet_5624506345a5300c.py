def _extract_url_and_title(self, text, start):
    idx = self._whitespace.match(text, start + 1).end()
    if idx == len(text):
        return None, None
    end_idx = idx
    has_anglebrackets = text[idx] == '<'
    if has_anglebrackets:
        end_idx = self._find_balanced(text, end_idx + 1, '<', '>')
    end_idx = self._find_balanced(text, end_idx, '(', ')')
    match = self._inline_link_title.search(text, idx, end_idx)
    if not match:
        return None, None
    url = text[idx:match.start()]
    if has_anglebrackets:
        url = self._strip_anglebrackets.sub('\\1', url)
    return url, end_idx