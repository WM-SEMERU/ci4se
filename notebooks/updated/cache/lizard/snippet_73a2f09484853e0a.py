def uninstall(ctx, module_list):
    modules.uninstall(ctx, module_list)
    ctx.log_line(
        'Deprecated: use anthem.lyrics.modules.uninstall instead of anthem.lyrics.uninstaller.uninstall'
        )