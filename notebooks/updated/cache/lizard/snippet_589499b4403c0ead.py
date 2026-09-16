def compile(checks):
    out = ['import check50']
    for name, check in checks.items():
        out.append(_compile_check(name, check))
    return '\n\n'.join(out)