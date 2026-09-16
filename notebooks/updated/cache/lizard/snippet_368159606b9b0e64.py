def write_shared_locations(self, paths, dry_run=False):
    shared_path = os.path.join(self.path, 'SHARED')
    logger.info('creating %s', shared_path)
    if dry_run:
        return None
    lines = []
    for key in ('prefix', 'lib', 'headers', 'scripts', 'data'):
        path = paths[key]
        if os.path.isdir(paths[key]):
            lines.append('%s=%s' % (key, path))
    for ns in paths.get('namespace', ()):
        lines.append('namespace=%s' % ns)
    with codecs.open(shared_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    return shared_path