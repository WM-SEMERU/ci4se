def tab_join(ToMerge, keycols=None, nullvals=None, renamer=None,
    returnrenaming=False, Names=None):
    [Result, Renaming] = spreadsheet.join(ToMerge, keycols=keycols,
        nullvals=nullvals, renamer=renamer, returnrenaming=True, Names=Names)
    if isinstance(ToMerge, dict):
        Names = ToMerge.keys()
    else:
        Names = range(len(ToMerge))
    Colorings = dict([((k, ToMerge[k].coloring) if 'coloring' in dir(
        ToMerge[k]) else {}) for k in Names])
    for k in Names:
        if k in Renaming.keys():
            l = ToMerge[k]
            Colorings[k] = dict([(g, [(n if not n in Renaming[k].keys() else
                Renaming[k][n]) for n in l.coloring[g]]) for g in Colorings
                [k].keys()])
    Coloring = {}
    for k in Colorings.keys():
        for j in Colorings[k].keys():
            if j in Coloring.keys():
                Coloring[j] = utils.uniqify(Coloring[j] + Colorings[k][j])
            else:
                Coloring[j] = utils.uniqify(Colorings[k][j])
    Result = Result.view(tabarray)
    Result.coloring = Coloring
    if returnrenaming:
        return [Result, Renaming]
    else:
        return Result