def read_reference_resource_list(self, ref_sitemap, name='reference'):
    rl = ResourceList()
    self.logger.info('Reading %s resource list from %s ...' % (name,
        ref_sitemap))
    rl.mapper = self.mapper
    rl.read(uri=ref_sitemap, index_only=not self.allow_multifile)
    num_entries = len(rl.resources)
    self.logger.info('Read %s resource list with %d entries in %d sitemaps' %
        (name, num_entries, rl.num_files))
    if self.verbose:
        to_show = 100
        override_str = ' (override with --max-sitemap-entries)'
        if self.max_sitemap_entries:
            to_show = self.max_sitemap_entries
            override_str = ''
        if num_entries > to_show:
            print('Showing first %d entries sorted by URI%s...' % (to_show,
                override_str))
        n = 0
        for r in rl.resources:
            print(r)
            n += 1
            if n >= to_show:
                break
    return rl