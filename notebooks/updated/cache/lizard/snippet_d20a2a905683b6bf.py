def export_losses_by_asset_npz(ekey, dstore):
    fname = dstore.export_path('%s.%s' % ekey)
    savez(fname, **dict(extract(dstore, 'losses_by_asset')))
    return [fname]