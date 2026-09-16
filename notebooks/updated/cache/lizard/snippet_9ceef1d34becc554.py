def upload(ctx):
    settings.add_cli_options(ctx.cli_options, settings.TransferAction.Upload)
    ctx.initialize(settings.TransferAction.Upload)
    specs = settings.create_upload_specifications(ctx.cli_options, ctx.config)
    del ctx.cli_options
    for spec in specs:
        blobxfer.api.Uploader(ctx.general_options, ctx.credentials, spec
            ).start()