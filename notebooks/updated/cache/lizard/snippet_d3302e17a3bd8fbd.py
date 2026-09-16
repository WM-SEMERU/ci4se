def get_parser(segmenter, **options):
    if segmenter == 'nlapi':
        return NLAPIParser(**options)
    elif segmenter == 'mecab':
        return MecabParser()
    elif segmenter == 'tinysegmenter':
        return TinysegmenterParser()
    else:
        raise ValueError('Segmenter {} is not supported.'.format(segmenter))