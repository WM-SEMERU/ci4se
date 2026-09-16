def filter_tagged_lines(tagged_lines, include_tags=None, exclude_tags=None):
    r
    include_tags = (include_tags,) if isinstance(include_tags, str
        ) else include_tags
    exclude_tags = (exclude_tags,) if isinstance(exclude_tags, str
        ) else exclude_tags
    for tagged_line in tagged_lines:
        if include_tags is None or tagged_line[0] in include_tags or any(
            tagged_line[0].startswith(t) for t in include_tags):
            if exclude_tags is None or not any(tagged_line[0].startswith(t) for
                t in exclude_tags):
                yield tagged_line
            else:
                logger.debug(
                    'skipping tag {} because it starts with one of the exclude_tags={}'
                    .format(tagged_line[0], exclude_tags))
        else:
            logger.debug('skipping tag {} because not in {}'.format(
                tagged_line[0], include_tags))