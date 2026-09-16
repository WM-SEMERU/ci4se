def extract(fileobj, keywords, comment_tags, options):
    extractor = BabelMakoExtractor(keywords, comment_tags, options)
    for message in extractor(fileobj):
        yield message