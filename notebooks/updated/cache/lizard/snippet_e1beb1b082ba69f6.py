def get_seaborn_colorbar(dfr, classes):
    levels = sorted(list(set(classes.values())))
    paldict = {lvl: pal for lvl, pal in zip(levels, sns.cubehelix_palette(
        len(levels), light=0.9, dark=0.1, reverse=True, start=1, rot=-2))}
    lvl_pal = {cls: paldict[lvl] for cls, lvl in list(classes.items())}
    col_cb = pd.Series(dfr.index).map(lvl_pal)
    col_cb.index = dfr.index
    return col_cb