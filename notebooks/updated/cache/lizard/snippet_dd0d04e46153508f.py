def stack_as_string():
    if sys.version_info.major == 3:
        stack = io.StringIO()
    else:
        stack = io.BytesIO()
    traceback.print_stack(file=stack)
    stack.seek(0)
    stack = stack.read()
    return stack