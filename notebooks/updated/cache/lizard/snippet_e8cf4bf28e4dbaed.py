def _wrap_element(self, result):
    if isinstance(result, lxml.html.HtmlElement):
        return Parser(result)
    else:
        return result