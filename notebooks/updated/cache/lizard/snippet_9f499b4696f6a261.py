def print_results(self, results, min_ratio=None, indent=False, pval=0.05,
    prt=sys.stdout):
    results_adj = self.get_adj_records(results, min_ratio, pval)
    self.print_results_adj(results_adj, indent, prt)