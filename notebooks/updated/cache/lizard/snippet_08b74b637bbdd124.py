def parse_xhtml_reaction_notes(entry):
    properties = {}
    if entry.xml_notes is not None:
        cobra_notes = dict(parse_xhtml_notes(entry))
        if 'subsystem' in cobra_notes:
            properties['subsystem'] = cobra_notes['subsystem']
        if 'gene_association' in cobra_notes:
            properties['genes'] = cobra_notes['gene_association']
        if 'ec_number' in cobra_notes:
            properties['ec'] = cobra_notes['ec_number']
        if 'authors' in cobra_notes:
            properties['authors'] = [a.strip() for a in cobra_notes[
                'authors'].split(';')]
        if 'confidence' in cobra_notes:
            try:
                value = int(cobra_notes['confidence'])
            except ValueError:
                logger.warning(
                    'Unable to parse confidence level for {} as an integer: {}'
                    .format(entry.id, cobra_notes['confidence']))
                value = cobra_notes['confidence']
            properties['confidence'] = value
    return properties