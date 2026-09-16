def _get_identical_contigs(self, hits_dict):
    equivalent_contigs = []
    for qry_name, containing in hits_dict.items():
        equivalent = set()
        for containing_name in containing:
            if containing_name in hits_dict and qry_name in hits_dict[
                containing_name]:
                equivalent.add(containing_name)
                equivalent.add(qry_name)
        if len(equivalent):
            equivalent_contigs.append(equivalent)
            equivalent_contigs = self._collapse_list_of_sets(equivalent_contigs
                )
    return equivalent_contigs