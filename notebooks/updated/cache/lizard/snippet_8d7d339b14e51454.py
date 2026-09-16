def do_uni_form(parser, token):
    token = token.split_contents()
    form = token.pop(1)
    try:
        helper = token.pop(1)
    except IndexError:
        helper = None
    return UniFormNode(form, helper)