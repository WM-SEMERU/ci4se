def search_prod_obsid(self, ins, obsid, pipeline):
    ins_prod = self.prod_table[ins]
    for prod in ins_prod:
        if prod['ob'] == obsid:
            return StoredProduct(**prod)
    else:
        raise NoResultFound('result for ob %i not found' % obsid)