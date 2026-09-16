def complete_info(self, text, line, begidx, endidx):
    opts = self.INFO_OPTS
    if not text:
        completions = opts
    else:
        completions = [f for f in opts if f.startswith(text)]
    return completions