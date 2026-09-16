def dump_bulk(cls, parent=None, keep_ids=True):
    qset = cls._get_serializable_model().get_tree(parent)
    ret, lnk = [], {}
    for pyobj in qset:
        serobj = serializers.serialize('python', [pyobj])[0]
        fields = serobj['fields']
        depth = fields['depth']
        del fields['lft']
        del fields['rgt']
        del fields['depth']
        del fields['tree_id']
        if 'id' in fields:
            del fields['id']
        newobj = {'data': fields}
        if keep_ids:
            newobj['id'] = serobj['pk']
        if not parent and depth == 1 or parent and depth == parent.depth:
            ret.append(newobj)
        else:
            parentobj = pyobj.get_parent()
            parentser = lnk[parentobj.pk]
            if 'children' not in parentser:
                parentser['children'] = []
            parentser['children'].append(newobj)
        lnk[pyobj.pk] = newobj
    return ret