def reduce_contexts(parent, local):
    context = {}
    for k, v in parent.items():
        if type(v) == dict:
            d = v.copy()
            d.update(local.get(k, {}))
            context[k] = d
        elif type(v) == list:
            context[k] = v + ensure_list(local.get(k, []))
        else:
            context[k] = local.get(k, v)
    for k in (set(local.keys()) - set(parent.keys())):
        context[k] = local[k]
    return context