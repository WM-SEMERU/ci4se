def _parse_heading(self):
    self._global |= contexts.GL_HEADING
    reset = self._head
    self._head += 1
    best = 1
    while self._read() == '=':
        best += 1
        self._head += 1
    context = contexts.HEADING_LEVEL_1 << min(best - 1, 5)
    try:
        title, level = self._parse(context)
    except BadRoute:
        self._head = reset + best - 1
        self._emit_text('=' * best)
    else:
        self._emit(tokens.HeadingStart(level=level))
        if level < best:
            self._emit_text('=' * (best - level))
        self._emit_all(title)
        self._emit(tokens.HeadingEnd())
    finally:
        self._global ^= contexts.GL_HEADING