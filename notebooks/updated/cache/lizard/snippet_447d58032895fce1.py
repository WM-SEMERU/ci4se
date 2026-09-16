def setChoice(key, *args):
    return And(lambda n: n in args, error=SCHEMA_RANGE_ERROR % (key, str(args))
        )