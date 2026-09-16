def translate_features_to_letter_annotations(protein, more_sites=None):
    from ssbio.databases.uniprot import longname_sites
    from collections import defaultdict
    sites = longname_sites
    sites.append('nucleotide phosphate-binding region')
    sites.append('DNA-binding region')
    sites.append('intramembrane region')
    sites.append('transmembrane region')
    sites.append('catalyticResidue')
    if more_sites:
        more_sites = ssbio.utils.force_list(more_sites)
        sites.extend(more_sites)
    sites = list(set(sites))
    for site in sites:
        protein.representative_sequence.letter_annotations[site] = [False
            ] * protein.representative_sequence.seq_len
    to_store = defaultdict(list)
    for f in protein.representative_sequence.features:
        if f.type in sites:
            to_store[f.type].append(f)
    for site, feature in to_store.items():
        try:
            positions = [int(f.location.start) for f in feature]
        except TypeError:
            log.error(
                'Protein {}, SeqProp {}: unable to translate feature {} into letter annotation'
                .format(protein.id, protein.representative_sequence.id, site))
            continue
        feat_letter_anno = []
        for x in range(protein.representative_sequence.seq_len):
            if x in positions:
                idx = positions.index(x)
                if 'description' in feature[idx].qualifiers:
                    feat_letter_anno.append(feature[idx].qualifiers[
                        'description'])
                else:
                    feat_letter_anno.append(True)
            else:
                feat_letter_anno.append(False)
        protein.representative_sequence.letter_annotations[site
            ] = feat_letter_anno