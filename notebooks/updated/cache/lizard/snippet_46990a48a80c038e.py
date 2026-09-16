def code_block(self, node, entering):
    if self.use_pygments:
        self.cr()
        info_words = node.info.split() if node.info else []
        if len(info_words) > 0 and len(info_words[0]) > 0:
            try:
                lexer = get_lexer_by_name(info_words[0])
            except ValueError:
                lexer = TextLexer()
        else:
            lexer = TextLexer()
        formatter = HtmlFormatter(**self.pygments_options)
        parsed = highlight(node.literal, lexer, formatter)
        self.lit(parsed)
        self.cr()
    else:
        super().code_block(node, entering)