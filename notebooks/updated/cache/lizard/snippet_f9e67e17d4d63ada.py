def download_and_compile_igraph(self):
    print('We will now try to download and compile the C core from scratch.')
    print('Version number of the C core: %s' % self.c_core_versions[0])
    if len(self.c_core_versions) > 1:
        print('We will also try: %s' % ', '.join(self.c_core_versions[1:]))
    print('')
    igraph_builder = IgraphCCoreBuilder(self.c_core_versions, self.
        c_core_url, show_progress_bar=self.show_progress_bar)
    if not igraph_builder.run():
        print('Could not download and compile the C core of igraph.')
        print('')
        return False
    else:
        return True