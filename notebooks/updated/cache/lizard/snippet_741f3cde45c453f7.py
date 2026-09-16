def _get_asset_size(self, asset_type):
    if asset_type == 'page':
        assets = self.entries
    else:
        assets = getattr(self, '{0}_files'.format(asset_type), None)
    return self.get_total_size(assets)