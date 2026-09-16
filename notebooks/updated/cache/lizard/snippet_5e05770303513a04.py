def _POInitBuilder(env, **kw):
    import SCons.Action
    from SCons.Tool.GettextCommon import _init_po_files, _POFileBuilder
    action = SCons.Action.Action(_init_po_files, None)
    return _POFileBuilder(env, action=action, target_alias='$POCREATE_ALIAS')