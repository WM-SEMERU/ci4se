def cli(ctx, id_number, new_key, metadata=''):
    return ctx.gi.cannedkeys.update_key(id_number, new_key, metadata=metadata)