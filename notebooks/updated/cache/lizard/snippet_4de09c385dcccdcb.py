def get_below_threshold(umi_quals, quality_encoding, quality_filter_threshold):
    umi_quals = [(x - RANGES[quality_encoding][0]) for x in map(ord, umi_quals)
        ]
    below_threshold = [(x < quality_filter_threshold) for x in umi_quals]
    return below_threshold