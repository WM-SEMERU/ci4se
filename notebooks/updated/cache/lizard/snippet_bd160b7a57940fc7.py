def infer_list_subtype(items):
    subtype = End
    for item in items:
        item_type = type(item)
        if not issubclass(item_type, Base):
            continue
        if subtype is End:
            subtype = item_type
            if not issubclass(subtype, List):
                return subtype
        elif subtype is not item_type:
            stype, itype = subtype, item_type
            generic = List
            while issubclass(stype, List) and issubclass(itype, List):
                stype, itype = stype.subtype, itype.subtype
                generic = List[generic]
            if stype is End:
                subtype = item_type
            elif itype is not End:
                return generic.subtype
    return subtype