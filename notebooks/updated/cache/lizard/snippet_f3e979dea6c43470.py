def format_info(raw):
    logging.debug(_('raw[0]: %s'), raw[0])
    results, sense = raw
    new = '\n'.join('{} {} {} {}'.format(i[0], sense.kind_id_to_name(i[1]),
        sense.file_id_to_name(i[2]).lower(), i[3] + ' ' if i[3] else '').
        strip() for i in results)
    return new