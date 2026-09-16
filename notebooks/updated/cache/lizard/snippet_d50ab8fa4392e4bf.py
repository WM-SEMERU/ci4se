def find_tokens(sentence, pattern):
    if not verify_pattern(pattern):
        raise PatternSyntaxException(pattern)

    def _match_node(t, p, tokens):
        pat_node = p.pop(0) if p else ''
        res = not pat_node or _match_token(t, pat_node, False) and (not p or
            _match_edge(t.children, p, tokens))
        if res and not p:
            tokens.append(t)
        return res

    def _match_edge(edges, p, tokens):
        pat_edge = p.pop(0) if p else ''
        if pat_edge:
            for t in edges:
                if _match_token(t, pat_edge, True):
                    _match_node(t, list(p), tokens)
                    if pat_edge == '**':
                        _match_edge(t.children, ['**'] + p, tokens)
    result_tokens = []
    _match_node(sentence.root, pattern.split('/'), result_tokens)
    return result_tokens