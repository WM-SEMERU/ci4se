def get_filter(self):
    args = []
    filter_kwargs = self.get_filter_kwargs()
    search = filter_kwargs.pop('search', None)
    if search and self.search_fields:
        search_args = []
        for f in self.search_fields:
            k = '%s__icontains' % f
            filter_kwargs.pop(k, None)
            q = Q(**{k: search})
            if search_args:
                q = search_args[0] | q
                search_args[0] = q
            else:
                search_args.append(q)
        args.append(search_args[0])
    if filter_kwargs:
        args.append(Q(**filter_kwargs))
    return args