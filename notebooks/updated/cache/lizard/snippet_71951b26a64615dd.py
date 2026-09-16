def get_rcntobj(self):
    if 'rcntobj' in self.kws:
        rcntobj = self.kws['rcntobj']
        if isinstance(rcntobj, CountRelatives):
            return rcntobj
        return CountRelatives(self.go2obj, self.relationships, dcnt='dcnt' in
            self.kw_elems, go2letter=self.kws.get('go2letter'))