def info_ratio(self, benchmark, ddof=0):
    diff = self.excess_ret(benchmark).anlzd_ret()
    return diff / self.tracking_error(benchmark, ddof=ddof)