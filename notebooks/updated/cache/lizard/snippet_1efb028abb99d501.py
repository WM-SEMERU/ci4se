def summarize_provenance_per_cache(self):
    provenance_summary = {}
    df = self.as_dataframe()
    for cache in self.cache_names:
        cache_name = self.cache_names[cache]
        cache_provenance = None
        num_discrepant = 0
        this_cache_dir = path.join(self.cache_dir, cache_name)
        if path.exists(this_cache_dir):
            for patient_id in self._list_patient_ids():
                patient_cache_dir = path.join(this_cache_dir, patient_id)
                try:
                    this_provenance = self.load_provenance(patient_cache_dir
                        =patient_cache_dir)
                except:
                    this_provenance = None
                if this_provenance:
                    if not cache_provenance:
                        cache_provenance = this_provenance
                    else:
                        num_discrepant += compare_provenance(this_provenance,
                            cache_provenance)
            if num_discrepant == 0:
                provenance_summary[cache_name] = cache_provenance
            else:
                provenance_summary[cache_name] = None
    return provenance_summary