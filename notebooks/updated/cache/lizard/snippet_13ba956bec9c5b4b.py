def announced_networks(self):
    return [(Element.from_href(ne.get('announced_ne_ref')), Element.
        from_href(ne.get('announced_rm_ref'))) for ne in self.data.get(
        'announced_ne_setting')]