def build_def_use(graph, lparams):
    analysis = reach_def_analysis(graph, lparams)
    UD = defaultdict(list)
    for node in graph.rpo:
        for i, ins in node.get_loc_with_ins():
            for var in ins.get_used_vars():
                if var not in analysis.def_to_loc:
                    continue
                ldefs = analysis.defs[node]
                prior_def = -1
                for v in ldefs.get(var, set()):
                    if prior_def < v < i:
                        prior_def = v
                if prior_def >= 0:
                    UD[var, i].append(prior_def)
                else:
                    intersect = analysis.def_to_loc[var].intersection(analysis
                        .R[node])
                    UD[var, i].extend(intersect)
    DU = defaultdict(list)
    for var_loc, defs_loc in UD.items():
        var, loc = var_loc
        for def_loc in defs_loc:
            DU[var, def_loc].append(loc)
    return UD, DU