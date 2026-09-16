def bhp2pascal(bhp, cfm, fan_tot_eff):
    inh2o = bhp * 6356.0 * fan_tot_eff / cfm
    pascal = inh2o2pascal(inh2o)
    m3s = cfm2m3s(cfm)
    return pascal, m3s