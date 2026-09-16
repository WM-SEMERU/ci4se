def check(text):
    err = 'misc.tense_present'
    msg = "'{}'."
    illogics = ['up to \\d{1,3}% ?[-—–]{0,3} ?(?:or|and) more\\W?',
        'between you and I', 'on accident', 'somewhat of a', "all it's own",
        'reason is because', 'audible to the ear', 'in regards to',
        'would of', "i ?(?:feel|am feeling|am|'m|'m feeling) nauseous"]
    errors = []
    for i in illogics:
        for m in re.finditer('\\s{}\\s'.format(i), text, flags=re.U | re.I):
            txt = m.group(0).strip()
            errors.append((m.start() + 1, m.end(), err, msg.format(txt), None))
    return errors