def main(ctx, connection):
    ctx.obj = Manager(connection=connection)
    ctx.obj.bind()