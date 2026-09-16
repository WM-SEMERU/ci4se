def collect_staticroot_removal(app, blueprints):
    collect_root = app.extensions['collect'].static_root
    return [bp for bp in blueprints if bp.has_static_folder and bp.
        static_folder != collect_root]