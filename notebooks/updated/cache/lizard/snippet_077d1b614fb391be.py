def compose_suffix(num_docs=0, num_topics=0, suffix=None):
    if not isinstance(suffix, basestring):
        suffix = '_{}X{}'.format(num_docs, num_topics)
    return suffix