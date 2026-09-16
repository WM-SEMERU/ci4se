def _get_ntgpadvals(self, flds, add_ns):
    is_set = False
    qualifiers = self._get_qualifier(flds[2])
    assert flds[3][:3] == 'GO:', 'UNRECOGNIZED GO({GO})'.format(GO=flds[3])
    db_reference = self._rd_fld_vals('DB_Reference', flds[4], is_set, 1)
    assert flds[5][:4] == 'ECO:', 'UNRECOGNIZED ECO({ECO})'.format(ECO=flds[3])
    with_from = self._rd_fld_vals('With_From', flds[6], is_set)
    taxons = self._get_taxon(flds[7])
    assert flds[8].isdigit(), 'UNRECOGNIZED DATE({D})'.format(D=flds[8])
    assert flds[9], '"Assigned By" VALUE WAS NOT FOUND'
    props = self._get_properties(flds[11])
    self._chk_qty_eq_1(flds, [0, 1, 3, 5, 8, 9])
    self._chk_qualifier(qualifiers)
    eco = flds[5]
    goid = flds[3]
    gpadvals = [flds[0], flds[1], qualifiers, flds[3], db_reference, eco,
        ECO2GRP[eco], with_from, taxons, GET_DATE_YYYYMMDD(flds[8]), flds[9
        ], get_extensions(flds[10]), props]
    if add_ns:
        goobj = self.godag.get(goid, '')
        gpadvals.append(NAMESPACE2NS[goobj.namespace] if goobj else '')
    return gpadvals