def read_phase(ph_file):
    ph_catalog = Catalog()
    f = open(ph_file, 'r')
    for line in f:
        if line[0] == '#':
            if 'event_text' not in locals():
                event_text = {'header': line.rstrip(), 'picks': []}
            else:
                ph_catalog.append(_phase_to_event(event_text))
                event_text = {'header': line.rstrip(), 'picks': []}
        else:
            event_text['picks'].append(line.rstrip())
    ph_catalog.append(_phase_to_event(event_text))
    return ph_catalog