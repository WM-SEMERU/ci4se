def specialspaceless(parser, token):
    nodelist = parser.parse(('endspecialspaceless',))
    parser.delete_first_token()
    return SpecialSpacelessNode(nodelist)