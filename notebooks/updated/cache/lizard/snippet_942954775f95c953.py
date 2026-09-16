def _filter_classes(cls_list, cls_type):
    for cls in cls_list:
        if isinstance(cls, type) and issubclass(cls, cls_type):
            if cls_type == TempyPlace and cls._base_place:
                pass
            else:
                yield cls