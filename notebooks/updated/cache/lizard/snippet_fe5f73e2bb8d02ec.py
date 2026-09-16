def _pop_comment_block(self, statements, header_re):
    res = []
    comments = []
    match = None
    st_iter = iter(statements)
    for st in st_iter:
        if isinstance(st, ast.Comment):
            match = header_re.match(st.text)
            if match:
                break
            else:
                res.append(st)
        else:
            res.append(st)
    for st in st_iter:
        if isinstance(st, ast.Comment):
            comments.append(st)
        else:
            res.append(st)
            break
    res.extend(list(st_iter))
    return match, dedent(''.join(c.text[1:] + '\n' for c in comments)), res