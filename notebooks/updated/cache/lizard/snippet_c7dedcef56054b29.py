def create_lxc_with_overlays(name, base, overlays, overlay_temp_path=None,
    service=None):
    service = service or LXCService
    if not overlays:
        raise TypeError("Argument 'overlays' must have at least one item")
    lxc_path = service.lxc_path()
    base_path = os.path.join(lxc_path, base)
    new_path = os.path.join(lxc_path, name)
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    overlay_group = OverlayGroup.create(new_path, base_path, overlays)
    initial_meta = dict(type='LXCWithOverlays', overlay_group=overlay_group
        .meta())
    meta = LXCMeta(initial=initial_meta)
    return LXCWithOverlays.with_meta(name, service, meta, overlay_group,
        save=True)