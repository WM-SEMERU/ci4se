def item_acl(self, item):
    if self.es_based:
        from nefertari_guards.elasticsearch import get_es_item_acl
        return get_es_item_acl(item)
    return super(DatabaseACLMixin, self).item_acl(item)