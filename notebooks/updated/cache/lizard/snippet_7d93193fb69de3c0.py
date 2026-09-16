def get_raw_data(self, section, scale=False):
    results = self.get_results()
    datasets = [None, None]
    if section == 'both':
        sections = ['template', 'complement']
    else:
        sections = [section]
    for n, this_section in enumerate(sections):
        if not results['has_{}'.format(this_section)]:
            continue
        start = results['first_sample_{}'.format(this_section)]
        dur = results['duration_{}'.format(this_section)]
        datasets[n] = self.handle.get_raw_data(start=start, end=start + dur,
            scale=scale)
    if section == 'both':
        return tuple(datasets)
    return datasets[0]