def execstr_funckw(func):
    import utool as ut
    funckw = ut.get_func_kwargs(func)
    return ut.execstr_dict(funckw, explicit=True)