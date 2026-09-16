def DEFINE_multi_float(name, default, help, lower_bound=None, upper_bound=
    None, flag_values=FLAGS, **args):
    parser = FloatParser(lower_bound, upper_bound)
    serializer = ArgumentSerializer()
    DEFINE_multi(parser, serializer, name, default, help, flag_values, **args)