def fire_hooks(ctx, document, elem, element, hooks):
    if not hooks:
        return
    for hook in hooks:
        hook(ctx, document, elem, element)