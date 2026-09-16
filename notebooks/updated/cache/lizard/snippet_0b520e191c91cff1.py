def get_mean_and_stddevs(self, sites, rup, dists, imt, stds_types):
    mean_list = []
    stddvs_list = []
    for period in self.avg_periods:
        imt_local = SA(float(period))
        mean, stddvs = self.gmpe.get_mean_and_stddevs(sites, rup, dists,
            imt_local, stds_types)
        mean_list.append(mean)
        stddvs_list.append(stddvs[0])
    mean_avgsa = 0.0
    stddvs_avgsa = 0.0
    for i1 in range(self.tnum):
        mean_avgsa += mean_list[i1]
        for i2 in range(self.tnum):
            rho = self.corr_func.get_correlation(self.avg_periods[i1], self
                .avg_periods[i2])
            stddvs_avgsa += rho * stddvs_list[i1] * stddvs_list[i2]
    mean_avgsa /= self.tnum
    stddvs_avgsa = np.sqrt(stddvs_avgsa) / self.tnum
    return mean_avgsa, [stddvs_avgsa]