def classical_damage(riskinputs, riskmodel, param, monitor):
    result = AccumDict(accum=AccumDict())
    for ri in riskinputs:
        for out in riskmodel.gen_outputs(ri, monitor):
            for l, loss_type in enumerate(riskmodel.loss_types):
                ordinals = ri.assets['ordinal']
                result[l, out.rlzi] += dict(zip(ordinals, out[loss_type]))
    return result