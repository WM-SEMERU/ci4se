def minify(drop_semi=True):
    layout_handlers = {OpenBlock: layout_handler_openbrace, CloseBlock:
        layout_handler_closebrace, EndStatement: layout_handler_semicolon,
        Space: layout_handler_space_minimum, OptionalSpace:
        layout_handler_space_minimum, RequiredSpace:
        layout_handler_space_imply, (Space, OpenBlock):
        layout_handler_openbrace, (Space, EndStatement):
        layout_handler_semicolon, (OptionalSpace, EndStatement):
        layout_handler_semicolon}
    if drop_semi:
        layout_handlers.update({EndStatement:
            layout_handler_semicolon_optional, (OptionalSpace, EndStatement
            ): layout_handler_semicolon_optional, (EndStatement, CloseBlock
            ): layout_handler_closebrace, (EndStatement, Dedent):
            rule_handler_noop, ((OptionalSpace, EndStatement), CloseBlock):
            layout_handler_closebrace})

    def minify_rule():
        return {'layout_handlers': layout_handlers, 'deferrable_handlers':
            {Literal: deferrable_handler_literal_continuation}}
    return minify_rule