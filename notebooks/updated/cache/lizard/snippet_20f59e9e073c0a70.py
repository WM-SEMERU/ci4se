def set_verbosity(v):
    try:
        new_level = int(v)
    except ValueError:
        new_level = converter.ABSL_NAMES[v.upper()]
    FLAGS.verbosity = new_level