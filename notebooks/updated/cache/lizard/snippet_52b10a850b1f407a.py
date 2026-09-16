def _quoted_text_handler_factory(delimiter, assertion, before, after,
    append_first=True, on_close=lambda ctx: None):

    @coroutine
    def quoted_text_handler(c, ctx, is_field_name=False):
        assert assertion(c)

        def append():
            if not _is_escaped_newline(c):
                val.append(c)
        is_clob = ctx.ion_type is IonType.CLOB
        max_char = _MAX_CLOB_CHAR if is_clob else _MAX_TEXT_CHAR
        ctx.set_unicode(quoted_text=True)
        val, event_on_close = before(c, ctx, is_field_name, is_clob)
        if append_first:
            append()
        c, self = yield
        trans = ctx.immediate_transition(self)
        done = False
        while not done:
            if c == delimiter and not _is_escaped(c):
                done = True
                if event_on_close:
                    trans = on_close(ctx)
                else:
                    break
            else:
                _validate_short_quoted_text(c, ctx, max_char)
                append()
            c, _ = yield trans
        yield after(c, ctx, is_field_name)
    return quoted_text_handler