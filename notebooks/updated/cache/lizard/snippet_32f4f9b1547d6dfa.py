def check(src, dst):
    was_bad = False
    try:
        _ = ast.parse(src)
    except Exception as exc:
        was_bad = True
        major, minor = sys.version_info[:2]
        logger.warning(
            "failed to parse source file with Python {0}.{1}'s builtin AST. Switch to manual or stop using deprecated Python 2 syntax. AST error message: {2}"
            .format(major, minor, exc))
    try:
        _ = ast.parse(dst)
    except Exception as exc:
        if was_bad:
            pass
        else:
            print(dst)
            logger.error(dst)
            raise