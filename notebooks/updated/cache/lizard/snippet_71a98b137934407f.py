def preview(self, limit=None, width=None):
    heading = self.heading
    rel = self.proj(*heading.non_blobs)
    if limit is None:
        limit = config['display.limit']
    if width is None:
        width = config['display.width']
    tuples = rel.fetch(limit=limit + 1, format='array')
    has_more = len(tuples) > limit
    tuples = tuples[:limit]
    columns = heading.names
    widths = {f: min(max([len(f)] + [len(str(e)) for e in tuples[f]] if f in
        tuples.dtype.names else [len('=BLOB=')]) + 4, width) for f in columns}
    templates = {f: ('%%-%d.%ds' % (widths[f], widths[f])) for f in columns}
    return ' '.join([(templates[f] % ('*' + f if f in rel.primary_key else
        f)) for f in columns]) + '\n' + ' '.join([('+' + '-' * (widths[
        column] - 2) + '+') for column in columns]) + '\n' + '\n'.join(' '.
        join(templates[f] % (tup[f] if f in tup.dtype.names else '=BLOB=') for
        f in columns) for tup in tuples) + ('\n   ...\n' if has_more else '\n'
        ) + (' (Total: %d)\n' % len(rel) if config[
        'display.show_tuple_count'] else '')