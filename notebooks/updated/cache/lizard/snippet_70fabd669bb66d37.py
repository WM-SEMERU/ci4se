def create_bundle(self, bundle_name, names=None, ca_only=True):
    if not names:
        if ca_only:
            names = []
            for name, record in self.store.store.items():
                if record['is_ca']:
                    names.append(name)
        else:
            names = self.store.store.keys()
    out_file_path = os.path.join(self.store.containing_dir, bundle_name)
    with open(out_file_path, 'w') as fh:
        for name in names:
            bundle = self.store.get_files(name)
            bundle.cert.load()
            fh.write(str(bundle.cert))
    return out_file_path