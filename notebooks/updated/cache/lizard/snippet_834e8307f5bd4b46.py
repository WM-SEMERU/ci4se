def _map_eom_terms(self, raw, limit=None):
    model = Model(self.graph)
    line_counter = 0
    with open(raw, 'r') as f1:
        f1.readline()
        for line in f1:
            line_counter += 1
            row = line.split('\t')
            (morphology_term_id, morphology_term_label, hp_id, hp_label, notes
                ) = row
            hp_id = re.sub('_', ':', hp_id)
            if re.match('.*HP:.*', hp_id):
                model.addClassToGraph(hp_id, None)
                model.addEquivalentClass(morphology_term_id, hp_id)
            else:
                LOG.warning('No matching HP term for %s', morphology_term_label
                    )
            if limit is not None and line_counter > limit:
                break
    return