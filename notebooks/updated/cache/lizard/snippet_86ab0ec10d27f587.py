def filter_entries(entries, config):

    def in_genus_list(species, genus_list):
        for genus in genus_list:
            if species.startswith(genus.capitalize()):
                return True
        return False
    new_entries = []
    for entry in entries:
        if config.type_material and config.type_material != ['any']:
            requested_types = map(lambda x: config.
                _RELATION_TO_TYPE_MATERIAL[x], config.type_material)
            if not entry['relation_to_type_material'] or entry[
                'relation_to_type_material'] not in requested_types:
                logging.debug(
                    'Skipping assembly with no reference to type material or reference to type material does not match requested'
                    )
                continue
            else:
                print(entry['relation_to_type_material'])
        if config.genus and not in_genus_list(entry['organism_name'],
            config.genus):
            logging.debug(
                'Organism name %r does not start with any in %r, skipping',
                entry['organism_name'], config.genus)
            continue
        if config.species_taxid and entry['species_taxid'
            ] not in config.species_taxid:
            logging.debug(
                'Species TaxID %r does not match with any in %r, skipping',
                entry['species_taxid'], config.species_taxid)
            continue
        if config.taxid and entry['taxid'] not in config.taxid:
            logging.debug(
                'Organism TaxID %r does not match with any in %r, skipping',
                entry['taxid'], config.taxid)
            continue
        if not config.is_compatible_assembly_accession(entry[
            'assembly_accession']):
            logging.debug(
                'Skipping entry with incompatible assembly accession %r',
                entry['assembly_accession'])
            continue
        if not config.is_compatible_assembly_level(entry['assembly_level']):
            logging.debug('Skipping entry with assembly level %r', entry[
                'assembly_level'])
            continue
        if config.refseq_category != 'all' and entry['refseq_category'
            ] != config.get_refseq_category_string(config.refseq_category):
            logging.debug('Skipping entry with refseq_category %r, not %r',
                entry['refseq_category'], config.refseq_category)
            continue
        new_entries.append(entry)
    return new_entries