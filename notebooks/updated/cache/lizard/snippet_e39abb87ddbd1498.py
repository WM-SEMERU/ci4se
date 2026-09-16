def catalogue_mt_filter(self, mt_table, flag=None):
    if flag is None:
        flag = np.ones(self.get_number_events(), dtype=bool)
    for comp_val in mt_table:
        id0 = np.logical_and(self.data['year'].astype(float) < comp_val[0],
            self.data['magnitude'] < comp_val[1])
        print(id0)
        flag[id0] = False
    if not np.all(flag):
        self.purge_catalogue(flag)