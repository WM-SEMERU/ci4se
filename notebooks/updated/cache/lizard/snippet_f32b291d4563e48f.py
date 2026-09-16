def alwaysCalledWithMatch(self, *args, **kwargs):
    self.__remove_args_first_item()
    alist, klist, gfunc = self.args, self.kwargs, self.__get_func
    if args and kwargs:
        return uch.tuple_partial_cmp_always(args, alist, gfunc
            ) and uch.dict_partial_cmp_always(kwargs, klist, gfunc)
    elif args:
        return uch.tuple_partial_cmp_always(args, alist, gfunc)
    elif kwargs:
        return uch.dict_partial_cmp_always(kwargs, klist, gfunc)
    else:
        ErrorHandler.called_with_empty_error()
    self.__get_func = SinonSpy.__get_by_matcher