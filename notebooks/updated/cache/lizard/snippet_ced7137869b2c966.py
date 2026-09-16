def is_uuid4(instr):
    v = instr.strip().replace('-', '').lower()
    if len(v) != 32:
        return False
    if not re.match('^[0-9a-f]+$', v):
        return False
    if v[12] != '4':
        return False
    if not re.match('[89ab]', v[16]):
        return False
    return True