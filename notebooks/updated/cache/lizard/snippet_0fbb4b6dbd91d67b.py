def _retrieve_remote(fnames):
    for fname in fnames:
        if objectstore.is_remote(fname):
            inputs = []
            regions = []
            remote_base = os.path.dirname(fname)
            for rfname in objectstore.list(remote_base):
                if rfname.endswith(tuple(KNOWN_EXTS.keys())):
                    inputs.append(rfname)
                elif rfname.endswith(('.bed', '.bed.gz')):
                    regions.append(rfname)
            return {'base': remote_base, 'inputs': inputs, 'region': 
                regions[0] if len(regions) == 1 else None}
    return {}