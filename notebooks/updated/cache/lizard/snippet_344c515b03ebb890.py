def _build_package_finder(self, options, index_urls, session):
    return PackageFinder(find_links=options.find_links, index_urls=
        index_urls, allow_all_prereleases=options.pre, trusted_hosts=
        options.trusted_hosts, session=session)