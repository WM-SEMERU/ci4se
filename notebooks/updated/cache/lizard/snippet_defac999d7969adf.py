def pager(parser, token):
    try:
        tag_name, page_obj = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            'pager tag requires 1 argument (page_obj), %s given' % (len(
            token.split_contents()) - 1))
    return PagerNode(page_obj)