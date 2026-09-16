def image(images, name=None, ch_axis=1, row=0, mode=None, batched=True, out
    =None, subdir='', timeout=5, **kwargs):
    from chainerui.report.image_report import check_available
    if not check_available():
        return
    from chainerui.report.image_report import report as _image
    out_root = _chainerui_asset_observer.get_outpath(out)
    out_path = os.path.join(out_root, subdir)
    if not os.path.isdir(out_path):
        os.makedirs(out_path)
    col_name = name
    if col_name is None:
        col_name = 'image'
    filename, created_at = _image(images, out_path, col_name, ch_axis, row,
        mode, batched)
    value = kwargs
    value['timestamp'] = created_at.isoformat()
    value['images'] = {col_name: os.path.join(subdir, filename)}
    _chainerui_asset_observer.add(value)
    _chainerui_asset_observer.save(out_root, timeout)