def sampler(dataframe, modulo, column='client_id', sample_id=42):
    return dataframe.withColumn('sampler', udf(lambda key: (crc32(key or ''
        ) & 4294967295) % modulo)(column)).where('sampler = %s' % sample_id
        ).drop('sampler')