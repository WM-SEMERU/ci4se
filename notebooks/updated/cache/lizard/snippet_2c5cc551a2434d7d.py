def _handle_codeblock(self, match):
    from pygments.lexers import get_lexer_by_name
    yield match.start(1), String, match.group(1)
    yield match.start(2), String, match.group(2)
    yield match.start(3), Text, match.group(3)
    lexer = None
    if self.handlecodeblocks:
        try:
            lexer = get_lexer_by_name(match.group(2).strip())
        except ClassNotFound:
            pass
    code = match.group(4)
    if lexer is None:
        yield match.start(4), String, code
        return
    for item in do_insertions([], lexer.get_tokens_unprocessed(code)):
        yield item
    yield match.start(5), String, match.group(5)