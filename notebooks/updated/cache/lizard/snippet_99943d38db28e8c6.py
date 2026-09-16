def combine_sources(sources, chunksize=None):
    r
    from pyemma.coordinates.data.sources_merger import SourcesMerger
    return SourcesMerger(sources, chunk=chunksize)