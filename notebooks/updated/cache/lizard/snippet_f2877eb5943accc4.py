def build(self):
    packages = self.packages()
    if packages:
        for pkg in packages:
            if not os.path.exists(self.meta.build_path):
                os.mkdir(self.meta.build_path)
            if not os.path.exists(self._SOURCES):
                os.mkdir(self._SOURCES)
            sbo_url = sbo_search_pkg(pkg)
            sbo_dwn = SBoLink(sbo_url).tar_gz()
            source_dwn = SBoGrep(pkg).source().split()
            sources = []
            os.chdir(self.meta.build_path)
            script = sbo_dwn.split('/')[-1]
            Download(self.meta.build_path, sbo_dwn.split(), repo='sbo').start()
            for src in source_dwn:
                Download(self._SOURCES, src.split(), repo='sbo').start()
                sources.append(src.split('/')[-1])
            BuildPackage(script, sources, self.meta.build_path, auto=False
                ).build()
    else:
        print('\nPackages not found in the queue for building\n')
        raise SystemExit(1)