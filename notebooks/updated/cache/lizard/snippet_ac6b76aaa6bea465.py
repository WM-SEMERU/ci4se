def filtered_rows_from_args(self, args):
    if len(self.manifests) == 0:
        print("fw: No manifests downloaded.  Try 'manifest download'")
        return None
    filters, remainder = self.filters_from_args(args)
    all = self.all_firmwares()
    rows = self.rows_for_firmwares(all)
    filtered = self.filter_rows(filters, rows)
    return filtered, remainder