def parse_reqs(filename):
    install_reqs = parse_requirements(filename, session=False)
    return [str(ir.req) for ir in install_reqs]