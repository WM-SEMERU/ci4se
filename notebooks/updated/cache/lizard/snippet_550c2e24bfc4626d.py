def get_catalog_nodes(self, catalog_id, ancestor_levels, descendant_levels,
    include_siblings):
    return objects.CatalogNode(self.get_catalog_node_ids(catalog_id=
        catalog_id, ancestor_levels=ancestor_levels, descendant_levels=
        descendant_levels, include_siblings=include_siblings)._my_map,
        runtime=self._runtime, proxy=self._proxy)