def deseq2_size_factors(counts, meta, design):
    import rpy2.robjects as r
    from rpy2.robjects import pandas2ri
    pandas2ri.activate()
    r.r('suppressMessages(library(DESeq2))')
    r.globalenv['counts'] = counts
    r.globalenv['meta'] = meta
    r.r('dds = DESeqDataSetFromMatrix(countData=counts, colData=meta, design={})'
        .format(design))
    r.r('dds = estimateSizeFactors(dds)')
    r.r('sf = sizeFactors(dds)')
    sf = r.globalenv['sf']
    return pd.Series(sf, index=counts.columns)