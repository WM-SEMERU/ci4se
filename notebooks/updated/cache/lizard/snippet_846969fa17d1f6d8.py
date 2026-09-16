def match_option_with_value(arguments, option, value):
    return '%s=%s' % (option, value) in arguments or contains_sublist(arguments
        , [option, value])