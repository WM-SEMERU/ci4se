def marvcli_user_rm(ctx, username):
    app = create_app()
    try:
        app.um.user_rm(username)
    except ValueError as e:
        ctx.fail(e.args[0])