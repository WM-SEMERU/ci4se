def _find_human_readable_labels(synsets, synset_to_human):
    humans = []
    for s in synsets:
        assert s in synset_to_human, 'Failed to find: %s' % s
        humans.append(synset_to_human[s])
    return humans