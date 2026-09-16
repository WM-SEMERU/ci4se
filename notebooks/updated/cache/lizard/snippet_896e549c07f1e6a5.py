def prune_topics(bag_topics, include, exclude):
    topics_to_use = set()
    if include is None:
        for t in bag_topics:
            topics_to_use.add(t)
    elif isinstance(include, basestring):
        check = re.compile(include)
        for t in bag_topics:
            if re.match(check, t) is not None:
                topics_to_use.add(t)
    else:
        try:
            for topic in include:
                if topic in bag_topics:
                    topics_to_use.add(topic)
        except:
            warnings.warn('Error in topic selection Using All!')
            topics_to_use = set()
            for t in bag_topics:
                topics_to_use.add(t)
    to_remove = set()
    if exclude is None:
        pass
    elif isinstance(exclude, basestring):
        check = re.compile(exclude)
        for t in list(topics_to_use):
            if re.match(check, t) is not None:
                to_remove.add(t)
    else:
        for remove in exclude:
            if remove in exclude:
                to_remove.add(remove)
    topics_to_use = topics_to_use - to_remove
    return list(topics_to_use)