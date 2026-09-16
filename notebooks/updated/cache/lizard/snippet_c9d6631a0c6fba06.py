def _get_pltdotstrs(self, hdrgos_usr, **kws):
    import datetime
    import timeit
    dotstrs_all = []
    tic = timeit.default_timer()
    hdrgo2usrgos, go2obj = self._get_plt_data(hdrgos_usr)
    for hdrgo, usrgos in hdrgo2usrgos.items():
        dotstrs_cur = self._get_dotgraphs(hdrgo, usrgos, pltargs=
            PltGroupedGosArgs(self.grprobj, **kws), go2parentids=
            get_go2parents_go2obj(go2obj))
        dotstrs_all.extend(dotstrs_cur)
    sys.stdout.write('\nElapsed HMS: {HMS} to write '.format(HMS=str(
        datetime.timedelta(seconds=timeit.default_timer() - tic))))
    sys.stdout.write('{P:5,} GO DAG plots for {H:>5,} GO grouping headers\n'
        .format(H=len(hdrgo2usrgos), P=len(dotstrs_all)))
    return sorted(set(dotstrs_all))