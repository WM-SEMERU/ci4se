def cybox_RAW_ft_handler(self, enrichment, fact, attr_info, add_fact_kargs):
    raw_value = add_fact_kargs['values'][0]
    if len(raw_value) >= RAW_DATA_TO_DB_FOR_LENGTH_LESS_THAN:
        value_hash, storage_location = write_large_value(raw_value, dingos.
            DINGOS_LARGE_VALUE_DESTINATION)
        add_fact_kargs['values'] = [(value_hash, storage_location)]
    return True