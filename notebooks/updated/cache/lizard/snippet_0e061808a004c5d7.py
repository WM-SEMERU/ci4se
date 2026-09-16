def cmdloop(self, intro=None):
    style = style_from_pygments(BasicStyle, style_dict)
    self.preloop()
    stop = None
    while not stop:
        line = prompt(get_prompt_tokens=get_prompt_tokens, lexer=lexer,
            get_bottom_toolbar_tokens=get_bottom_toolbar_tokens, history=
            history, style=style, true_color=True, on_exit='return-none',
            on_abort='return-none', completer=QCompleter())
        if line is None or line.strip() == '\\\\':
            raise SystemExit
        else:
            line = self.precmd(line)
            stop = self.onecmd(line)
        stop = self.postcmd(stop, line)
    self.postloop()