def winapi(context, names):
    logging.info(_('Entering winapi mode'))
    sense = context.obj['sense']
    none = True
    for name in names:
        code = sense.query_args(name)
        if code:
            none = False
            print(stylify_code(code))
        else:
            logging.warning(_('Function not found: %s'), name)
    sys.exit(1 if none else 0)