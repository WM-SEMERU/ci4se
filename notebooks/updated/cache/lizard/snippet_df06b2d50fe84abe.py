def pivot_and_annotate(self, values, gpl, annotation_column, gpl_on='ID',
    gsm_on='ID_REF'):
    if isinstance(gpl, GPL):
        annotation_table = gpl.table
    elif isinstance(gpl, DataFrame):
        annotation_table = gpl
    else:
        raise TypeError('gpl should be a GPL object or a pandas.DataFrame')
    pivoted_samples = self.pivot_samples(values=values, index=gsm_on)
    ndf = pivoted_samples.reset_index().merge(annotation_table[[gpl_on,
        annotation_column]], left_on=gsm_on, right_on=gpl_on).set_index(gsm_on)
    del ndf[gpl_on]
    ndf.columns.name = 'name'
    return ndf