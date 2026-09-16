def opcode_check(l):
    if abs(PYTHON_VERSION - l['python_version']) <= 0.01 and IS_PYPY == l[
        'is_pypy']:
        try:
            import dis
            opmap = fix_opcode_names(dis.opmap)
            assert all(item in opmap.items() for item in l['opmap'].items())
            assert all(item in l['opmap'].items() for item in opmap.items())
        except:
            import sys