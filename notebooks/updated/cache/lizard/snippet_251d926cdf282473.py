def scenario_risk(riskinputs, riskmodel, param, monitor):
    E = param['E']
    L = len(riskmodel.loss_types)
    result = dict(agg=numpy.zeros((E, L), F32), avg=[], all_losses=
        AccumDict(accum={}))
    for ri in riskinputs:
        for out in riskmodel.gen_outputs(ri, monitor, param['epspath']):
            r = out.rlzi
            weight = param['weights'][r]
            slc = param['event_slice'](r)
            for l, loss_type in enumerate(riskmodel.loss_types):
                losses = out[loss_type]
                if numpy.product(losses.shape) == 0:
                    continue
                stats = numpy.zeros(len(ri.assets), stat_dt)
                for a, asset in enumerate(ri.assets):
                    stats['mean'][a] = losses[a].mean()
                    stats['stddev'][a] = losses[a].std(ddof=1)
                    result['avg'].append((l, r, asset['ordinal'], stats[a]))
                agglosses = losses.sum(axis=0)
                result['agg'][slc, l] += agglosses * weight
                if param['asset_loss_table']:
                    aids = ri.assets['ordinal']
                    result['all_losses'][l, r] += AccumDict(zip(aids, losses))
    return result