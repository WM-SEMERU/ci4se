def _sanitize(recipe):
    recipe = recipe.copy()
    for k in list(recipe):
        if k not in ('start', 'error') and int(k) and k != int(k):
            recipe[int(k)] = recipe[k]
            del recipe[k]
    for k in list(recipe):
        if 'output' in recipe[k] and not isinstance(recipe[k]['output'], (
            list, dict)):
            recipe[k]['output'] = [recipe[k]['output']]
    if 'start' in recipe:
        recipe['start'] = [tuple(x) for x in recipe['start']]
    return recipe