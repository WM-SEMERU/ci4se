def in_venv():
    global _in_venv
    if _in_venv is not None:
        return _in_venv
    if not (os.path.isfile(ORIG_PREFIX_TXT) or os.path.isfile(PY_VENV_CFG)):
        logger.debug('in_venv no orig_prefix_txt [%s]', ORIG_PREFIX_TXT)
        logger.debug('in_venv no py_venv_cfg [%s]', PY_VENV_CFG)
        _in_venv = False
        return _in_venv
    if 'VIRTUAL_ENV' in os.environ:
        logger.debug('in_venv VIRTUAL_ENV set.')
        _in_venv = True
    else:
        python = basename(sys.executable)
        for p in os.environ['PATH'].split(os.pathsep):
            py_path = join(p, python)
            if isfile(py_path):
                logger.debug('in_venv py_at [%s] return: %s', (py_path, sys
                    .executable != py_path))
                _in_venv = sys.executable != py_path
                break
    return _in_venv