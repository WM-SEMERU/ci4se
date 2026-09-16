def create_entry(group, name, timestamp, **attributes):
    from h5py import h5p, h5g, _hl
    try:
        gcpl = h5p.create(h5p.GROUP_CREATE)
        gcpl.set_link_creation_order(h5p.CRT_ORDER_TRACKED | h5p.
            CRT_ORDER_INDEXED)
    except AttributeError:
        grp = group.create_group(name)
    else:
        name, lcpl = group._e(name, lcpl=True)
        grp = _hl.group.Group(h5g.create(group.id, name, lcpl=lcpl, gcpl=gcpl))
    set_uuid(grp, attributes.pop('uuid', None))
    set_attributes(grp, timestamp=convert_timestamp(timestamp), **attributes)
    return grp