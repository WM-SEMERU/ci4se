def evaluate_code(self, code):
    if not code:
        return False
    LOGGER.debug('> Evaluating given code.')
    code = code.endswith('\n') and code or '{0}\n'.format(code)
    code = code.split('\n', 3)
    for i, line in enumerate(code[:-2]):
        if 'coding' in line:
            code[i] = line.replace('=', '\\=').replace(':', '\\:')
            break
    code = '\n'.join(code)
    sys.stdout.write(code)
    self.__console.runcode(code)
    return True