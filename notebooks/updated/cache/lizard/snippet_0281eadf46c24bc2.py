def workspace_add_file(ctx, file_grp, file_id, mimetype, page_id, force,
    local_filename):
    workspace = Workspace(ctx.resolver, directory=ctx.directory,
        mets_basename=ctx.mets_basename, automatic_backup=ctx.automatic_backup)
    if not local_filename.startswith(ctx.directory):
        log.debug("File '%s' is not in workspace, copying", local_filename)
        local_filename = ctx.resolver.download_to_directory(ctx.directory, 
            'file://' + local_filename, subdir=file_grp)
    url = 'file://' + local_filename
    workspace.mets.add_file(fileGrp=file_grp, ID=file_id, mimetype=mimetype,
        url=url, pageId=page_id, force=force, local_filename=local_filename)
    workspace.save_mets()