def cli(ctx, group_id, new_name):
    return ctx.gi.groups.update_group(group_id, new_name)