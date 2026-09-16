def to_strings(self, resource):
    collections = self.__collect(resource)
    rpr_map = OrderedDict()
    for mb_cls, coll in iteritems_(collections):
        strm = NativeIO('w')
        dump_resource(coll, strm, content_type=self.__content_type)
        rpr_map[mb_cls] = strm.getvalue()
    return rpr_map