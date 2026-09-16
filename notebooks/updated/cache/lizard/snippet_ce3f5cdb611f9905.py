def visitLexerAtom(self, ctx: jsgParser.LexerAtomContext):
    if ctx.LEXER_CHAR_SET() or ctx.ANY():
        self._rulePattern += str(ctx.getText())
    else:
        self.visitChildren(ctx)