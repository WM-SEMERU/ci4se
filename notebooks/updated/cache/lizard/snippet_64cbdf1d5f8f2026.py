def if_relationship(parser, token):
    bits = list(token.split_contents())
    if len(bits) != 4:
        raise TemplateSyntaxError('%r takes 3 arguments:\n%s' % (bits[0],
            if_relationship.__doc__))
    end_tag = 'end' + bits[0]
    nodelist_true = parser.parse(('else', end_tag))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse((end_tag,))
        parser.delete_first_token()
    else:
        nodelist_false = template.NodeList()
    return IfRelationshipNode(nodelist_true, nodelist_false, *bits[1:])