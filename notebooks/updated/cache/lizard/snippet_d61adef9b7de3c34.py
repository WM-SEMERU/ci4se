def ast_to_html(self, ast, link_resolver):
    out, _ = cmark.ast_to_html(ast, link_resolver)
    return out