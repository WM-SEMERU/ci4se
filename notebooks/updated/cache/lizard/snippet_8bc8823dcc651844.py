def nice_number_string(number, decimal_places=2):
    if number == np.round(number):
        return str(int(number))
    elif number < 1 and number > 0:
        inverse = 1 / number
        if int(inverse) == np.round(inverse):
            return '\\frac{{1}}{{{}}}'.format(int(inverse))
    else:
        template = '{{:.{0}}}'.format(decimal_places)
        return template.format(number)