def view_status_code(codes):
    if ',' not in codes:
        try:
            code = int(codes)
        except ValueError:
            return Response('Invalid status code', status=400)
        return status_code(code)
    choices = []
    for choice in codes.split(','):
        if ':' not in choice:
            code = choice
            weight = 1
        else:
            code, weight = choice.split(':')
        try:
            choices.append((int(code), float(weight)))
        except ValueError:
            return Response('Invalid status code', status=400)
    code = weighted_choice(choices)
    return status_code(code)