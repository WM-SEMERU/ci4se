def _fetch_pkg(self, gopath, pkg, rev):
    fetcher = self._get_fetcher(pkg)
    root = fetcher.root()
    root_dir = os.path.join(self.workdir, 'fetches', root, rev)
    if not os.path.exists(root_dir):
        with temporary_dir() as tmp_fetch_root:
            with self.context.new_workunit('fetch {}'.format(pkg)):
                fetcher.fetch(dest=tmp_fetch_root, rev=rev)
                safe_mkdir(root_dir)
                for path in os.listdir(tmp_fetch_root):
                    shutil.move(os.path.join(tmp_fetch_root, path), os.path
                        .join(root_dir, path))
    dest_dir = os.path.join(gopath, 'src', root)
    safe_mkdir(dest_dir, clean=True)
    for path in os.listdir(root_dir):
        os.symlink(os.path.join(root_dir, path), os.path.join(dest_dir, path))