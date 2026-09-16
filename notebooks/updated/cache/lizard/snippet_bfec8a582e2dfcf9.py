def extract_spellout_values(text):
    values = []
    for item in r.REG_TXT.finditer(text):
        surface, span = clean_surface(item.group(0), item.span())
        if not surface or surface.lower() in r.SCALES:
            continue
        curr = result = 0.0
        for word in surface.split():
            try:
                scale, increment = 1, float(word.lower())
            except ValueError:
                scale, increment = r.NUMWORDS[word.lower()]
            curr = curr * scale + increment
            if scale > 100:
                result += curr
                curr = 0.0
        values.append({'old_surface': surface, 'old_span': span,
            'new_surface': unicode(result + curr)})
    for item in re.finditer('\\d+(,\\d{3})+', text):
        values.append({'old_surface': item.group(0), 'old_span': item.span(
            ), 'new_surface': unicode(item.group(0).replace(',', ''))})
    return sorted(values, key=lambda x: x['old_span'][0])