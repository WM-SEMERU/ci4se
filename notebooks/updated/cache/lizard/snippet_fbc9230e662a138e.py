def _load_single_patient_variants(self, patient, filter_fn, use_cache=True,
    **kwargs):
    if filter_fn is None:
        use_filtered_cache = False
    else:
        filter_fn_name = self._get_function_name(filter_fn)
        logger.debug('loading variants for patient {} with filter_fn {}'.
            format(patient.id, filter_fn_name))
        use_filtered_cache = use_cache
    if use_filtered_cache:
        logger.debug('... identifying filtered-cache file name')
        try:
            filtered_cache_file_name = '%s-variants.%s.pkl' % (self.
                merge_type, self._hash_filter_fn(filter_fn, **kwargs))
        except:
            logger.warning(
                '... error identifying filtered-cache file name for patient {}: {}'
                .format(patient.id, filter_fn_name))
            use_filtered_cache = False
        else:
            logger.debug('... trying to load filtered variants from cache: {}'
                .format(filtered_cache_file_name))
            try:
                cached = self.load_from_cache(self.cache_names['variant'],
                    patient.id, filtered_cache_file_name)
                if cached is not None:
                    return cached
            except:
                logger.warning(
                    'Error loading variants from cache for patient: {}'.
                    format(patient.id))
                pass
    logger.debug('... getting merged variants for: {}'.format(patient.id))
    merged_variants = self._load_single_patient_merged_variants(patient,
        use_cache=use_cache)
    if merged_variants is None:
        logger.info('Variants did not exist for patient %s' % patient.id)
        return None
    logger.debug('... applying filters to variants for: {}'.format(patient.id))
    filtered_variants = filter_variants(variant_collection=merged_variants,
        patient=patient, filter_fn=filter_fn, **kwargs)
    if use_filtered_cache:
        logger.debug('... saving filtered variants to cache: {}'.format(
            filtered_cache_file_name))
        self.save_to_cache(filtered_variants, self.cache_names['variant'],
            patient.id, filtered_cache_file_name)
    return filtered_variants