def cache_relationships(self, cache_super=True, cache_sub=True):
    relationships_to_cache = compress(['super_relationships__super_entity',
        'sub_relationships__sub_entity'], [cache_super, cache_sub])
    return self.prefetch_related(*relationships_to_cache)