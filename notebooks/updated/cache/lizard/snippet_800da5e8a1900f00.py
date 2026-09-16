def select_extended(cat_table):
    try:
        l = [(len(row.strip()) > 0) for row in cat_table[
            'Extended_Source_Name'].data]
        return np.array(l, bool)
    except KeyError:
        return cat_table['Extended']