def _list_sessions(self):
    sformats = formats.SESSION_FORMATS
    tmux_formats = [('#{%s}' % f) for f in sformats]
    tmux_args = '-F%s' % '\t'.join(tmux_formats),
    proc = self.cmd('list-sessions', *tmux_args)
    if proc.stderr:
        raise exc.LibTmuxException(proc.stderr)
    sformats = formats.SESSION_FORMATS
    tmux_formats = [('#{%s}' % format) for format in sformats]
    sessions = proc.stdout
    sessions = [dict(zip(sformats, session.split('\t'))) for session in
        sessions]
    sessions = [dict((k, v) for k, v in session.items() if v) for session in
        sessions]
    return sessions