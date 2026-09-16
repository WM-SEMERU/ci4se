def check_exclamations_ppm(text):
    err = 'leonard.exclamation.30ppm'
    msg = 'More than 30 ppm of exclamations. Keep them under control.'
    regex = '\\w!'
    count = len(re.findall(regex, text))
    num_words = len(text.split(' '))
    ppm = count * 1.0 / num_words * 1000000.0
    if ppm > 30 and count > 1:
        loc = re.search(regex, text).start() + 1
        return [(loc, loc + 1, err, msg, '.')]
    else:
        return []