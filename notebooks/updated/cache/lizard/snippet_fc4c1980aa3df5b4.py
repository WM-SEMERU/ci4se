def _add_singles_to_buffer(self, results, ifos):
    if len(self.singles.keys()) == 0:
        self.set_singles_buffer(results)
    logging.info('adding singles to the background estimate...')
    updated_indices = {}
    for ifo in ifos:
        trigs = results[ifo]
        if len(trigs['snr'] > 0):
            trigsc = copy.copy(trigs)
            trigsc['chisq'] = trigs['chisq'] * trigs['chisq_dof']
            trigsc['chisq_dof'] = (trigs['chisq_dof'] + 2) / 2
            single_stat = self.stat_calculator.single(trigsc)
        else:
            single_stat = numpy.array([], ndmin=1, dtype=self.
                stat_calculator.single_dtype)
        trigs['stat'] = single_stat
        data = numpy.zeros(len(single_stat), dtype=self.singles_dtype)
        for key, value in trigs.items():
            data[key] = value
        self.singles[ifo].add(trigs['template_id'], data)
        updated_indices[ifo] = trigs['template_id']
    return updated_indices