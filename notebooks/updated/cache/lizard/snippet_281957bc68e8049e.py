def do_execute(self, code, silent, store_history=True, user_expressions=
    None, allow_stdin=False):
    self._klog.info('[%.30s] [%d] [%s]', code, silent, user_expressions)
    code_noc = [line.strip() for line in code.split('\n') if line and line[
        0] != '#']
    if not code_noc:
        return self._send(None)
    try:
        magic_lines = []
        for line in code_noc:
            if line[0] != '%':
                break
            magic_lines.append(line)
        if magic_lines:
            out = [self._k.magic(line) for line in magic_lines]
            self._send(out, 'multi', silent=silent)
            code = '\n'.join(code_noc[len(magic_lines):])
        result = self._k.query(code, num=self.execution_count
            ) if code else None
        return self._send(result, 'raw', silent=silent)
    except Exception as e:
        return self._send(e, 'error', silent=silent)