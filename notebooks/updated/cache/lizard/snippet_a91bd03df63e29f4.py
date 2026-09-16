def check_messages(filename, report_empty=False):
    problems = []
    pomsgs = polib.pofile(filename)
    for msg in pomsgs:
        if astral(msg.msgstr):
            problems.append(('Non-BMP char', msg.msgid, msg.msgstr))
        if is_format_message(msg):
            continue
        if msg.msgid_plural:
            source = msg.msgid + ' | ' + msg.msgid_plural
            translation = ' | '.join(v for k, v in sorted(msg.msgstr_plural
                .items()))
            empty = any(not t.strip() for t in msg.msgstr_plural.values())
        else:
            source = msg.msgid
            translation = msg.msgstr
            empty = not msg.msgstr.strip()
        if empty:
            if report_empty:
                problems.append(('Empty translation', source))
        else:
            id_tags = tags_in_string(source)
            tx_tags = tags_in_string(translation)
            if id_tags != tx_tags:
                id_has = ', '.join(sorted('"{}"'.format(t) for t in id_tags -
                    tx_tags))
                tx_has = ', '.join(sorted('"{}"'.format(t) for t in tx_tags -
                    id_tags))
                if id_has and tx_has:
                    diff = '{} vs {}'.format(id_has, tx_has)
                elif id_has:
                    diff = '{} missing'.format(id_has)
                else:
                    diff = '{} added'.format(tx_has)
                problems.append(('Different tags in source and translation',
                    source, translation, diff))
    return problems