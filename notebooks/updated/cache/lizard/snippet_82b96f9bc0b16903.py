def strip_comments(tokens):
    prev_typ = None
    prev_end_col = 0
    for typ, tok, (start_row, start_col), (end_row, end_col), line in tokens:
        if typ in (tokenize.NL, tokenize.NEWLINE):
            if prev_typ in (tokenize.NL, tokenize.NEWLINE):
                start_col = 0
            else:
                start_col = prev_end_col
            end_col = start_col + 1
        elif typ == tokenize.COMMENT and start_row > 2:
            continue
        prev_typ = typ
        prev_end_col = end_col
        yield typ, tok, (start_row, start_col), (end_row, end_col), line