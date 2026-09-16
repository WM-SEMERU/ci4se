def get_requirements(filename=None):
    if filename is None:
        filename = 'requirements.txt'
    file = WORK_DIR / filename
    install_reqs = parse_requirements(str(file), session='hack')
    return [str(ir.req) for ir in install_reqs]