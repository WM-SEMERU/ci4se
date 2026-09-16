def sampling_query(sql, context, fields=None, count=5, sampling=None, udfs=
    None, data_sources=None):
    return Query(_sampling.Sampling.sampling_query(sql, fields, count,
        sampling), context=context, udfs=udfs, data_sources=data_sources)