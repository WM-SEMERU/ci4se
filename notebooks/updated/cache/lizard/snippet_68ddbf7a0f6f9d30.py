def get_molo_comments(parser, token):
    keywords = token.contents.split()
    if len(keywords) != 5 and len(keywords) != 7 and len(keywords) != 9:
        raise template.TemplateSyntaxError(
            "'%s' tag takes exactly 2,4 or 6 arguments" % (keywords[0],))
    if keywords[1] != 'for':
        raise template.TemplateSyntaxError(
            "first argument to '%s' tag must be 'for'" % (keywords[0],))
    if keywords[3] != 'as':
        raise template.TemplateSyntaxError(
            "first argument to '%s' tag must be 'as'" % (keywords[0],))
    if len(keywords) > 5 and keywords[5] != 'limit':
        raise template.TemplateSyntaxError(
            "third argument to '%s' tag must be 'limit'" % (keywords[0],))
    if len(keywords) == 7:
        return GetMoloCommentsNode(keywords[2], keywords[4], keywords[6])
    if len(keywords) > 7 and keywords[7] != 'child_limit':
        raise template.TemplateSyntaxError(
            "third argument to '%s' tag must be 'child_limit'" % (keywords[0],)
            )
    if len(keywords) > 7:
        return GetMoloCommentsNode(keywords[2], keywords[4], keywords[6],
            keywords[8])
    return GetMoloCommentsNode(keywords[2], keywords[4])