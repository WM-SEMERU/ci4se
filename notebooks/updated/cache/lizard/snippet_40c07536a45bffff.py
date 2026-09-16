def _pop_comment(self, statements, comment_re):
    res = []
    match = None
    for st in statements:
        if match or not isinstance(st, ast.Comment):
            res.append(st)
            continue
        match = comment_re.match(st.text)
        if not match:
            res.append(st)
    return match, res