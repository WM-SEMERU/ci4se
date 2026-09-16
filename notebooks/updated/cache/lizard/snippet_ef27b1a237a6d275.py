def _complete_history(self, cmd, args, text):
    if args:
        return
    return [x for x in {'clear', 'clearall'} if x.startswith(text)]