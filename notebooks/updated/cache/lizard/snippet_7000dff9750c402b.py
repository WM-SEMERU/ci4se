def SelectFieldPrompt(field_name, context_str, *options):
    option_format_str = '[ {} ] "{}"'
    option_dict = {}
    print(context_str)
    print('Please select one of the following options for field "{}"'.
        format(field_name))
    for cnt, option in enumerate(options):
        option_dict['{}'.format(cnt + 1)] = option
        if not callable(option):
            print(option_format_str.format(cnt + 1, u(str(option))))
        else:
            print(option_format_str.format(cnt + 1, option.__name__))
    choice = None
    while choice not in option_dict:
        choice = input('option> ').strip()
    new_value = option_dict[choice]
    if callable(new_value):
        return new_value()
    else:
        return new_value