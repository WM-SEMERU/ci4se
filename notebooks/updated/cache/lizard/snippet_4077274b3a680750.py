def get_text_range(self, node):
    if not hasattr(node, 'first_token'):
        return 0, 0
    start = node.first_token.startpos
    if any(match_token(t, token.NEWLINE) for t in self.get_tokens(node)):
        start = self._text.rfind('\n', 0, start) + 1
    return start, node.last_token.endpos