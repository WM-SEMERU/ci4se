def minifyspace(parser, token):
    nodelist = parser.parse(('endminifyspace',))
    parser.delete_first_token()
    return MinifiedNode(nodelist)