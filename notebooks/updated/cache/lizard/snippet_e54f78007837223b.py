def _build_dispatch_map(self):
    return {'_'.join(a.split('_')[1:]): getattr(self, a) for a in dir(self) if
        a.startswith('parse_')}