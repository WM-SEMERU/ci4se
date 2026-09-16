def seq_include(records, filter_regex):
    regex = re.compile(filter_regex)
    for record in records:
        if regex.search(str(record.seq)):
            yield record