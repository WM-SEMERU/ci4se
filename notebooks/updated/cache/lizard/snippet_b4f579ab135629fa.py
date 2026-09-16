def comment_to_ast(self, comment, link_resolver):
    assert comment is not None
    text = comment.description
    if self.remove_xml_tags or comment.filename in self.gdbus_codegen_sources:
        text = re.sub('<.*?>', '', text)
    if self.escape_html:
        text = cgi.escape(text)
    ast, diagnostics = cmark.gtkdoc_to_ast(text, link_resolver)
    for diag in diagnostics:
        if (comment.filename and comment.filename not in self.
            gdbus_codegen_sources):
            column = diag.column + comment.col_offset
            if diag.lineno == 0:
                column += comment.initial_col_offset
            lines = text.split('\n')
            line = lines[diag.lineno]
            i = 0
            while line[i] == ' ':
                i += 1
            column += i - 1
            if diag.lineno > 0 and any([(c != ' ') for c in lines[diag.
                lineno - 1]]):
                column += 1
            lineno = -1
            if comment.lineno != -1:
                lineno = comment.lineno - 1 + comment.line_offset + diag.lineno
            warn(diag.code, message=diag.message, filename=comment.filename,
                lineno=lineno, column=column)
    return ast