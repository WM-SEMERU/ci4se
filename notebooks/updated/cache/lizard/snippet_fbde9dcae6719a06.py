def format_formula(formula):
    formatted_formula = ''
    number_format = ''
    for i, s in enumerate(formula):
        if s.isdigit():
            if not number_format:
                number_format = '_{'
            number_format += s
            if i == len(formula) - 1:
                number_format += '}'
                formatted_formula += number_format
        else:
            if number_format:
                number_format += '}'
                formatted_formula += number_format
                number_format = ''
            formatted_formula += s
    return '$%s$' % formatted_formula