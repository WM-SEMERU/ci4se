def import_spydercustomize():
    here = osp.dirname(__file__)
    parent = osp.dirname(here)
    customize_dir = osp.join(parent, 'customize')
    while '' in sys.path:
        sys.path.remove('')
    site.addsitedir(customize_dir)
    import spydercustomize
    try:
        sys.path.remove(customize_dir)
    except ValueError:
        pass