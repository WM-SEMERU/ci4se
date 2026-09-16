def cnv_to_event(name, data):
    cur_ploidy = ploidy.get_ploidy([data])
    if name.startswith('cnv'):
        num = max([int(x) for x in name.split('_')[0].replace('cnv', '').
            split(';')])
        if num < cur_ploidy:
            return 'DEL'
        elif num > cur_ploidy:
            return 'DUP'
        else:
            return name
    else:
        return name