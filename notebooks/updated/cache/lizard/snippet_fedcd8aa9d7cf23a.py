def export_kappa_cm(model, fname=None):
    from .kappa_util import cm_json_to_graph
    kappa = _prepare_kappa(model)
    cmap = kappa.analyses_contact_map()
    cm = cm_json_to_graph(cmap)
    if fname:
        cm.draw(fname, prog='dot')
    return cm