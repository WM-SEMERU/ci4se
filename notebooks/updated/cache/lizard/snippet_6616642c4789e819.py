def slp_frag(self, time=None):
    epochs = self.get_epochs(time=time)
    stage_int = {'Wake': 0, 'NREM1': 1, 'NREM2': 2, 'NREM3': 3, 'REM': 2}
    hypno_str = [x['stage'] for x in epochs if x['stage'] in stage_int.keys()]
    hypno_int = [stage_int[x] for x in hypno_str]
    frag = sum(asarray(clip(diff(hypno_int), a_min=None, a_max=0), dtype=bool))
    n3_to_rem = 0
    for i, j in enumerate(hypno_str[:-1]):
        if j == 'NREM3':
            if hypno_str[i + 1] == 'REM':
                n3_to_rem += 1
    return frag - n3_to_rem