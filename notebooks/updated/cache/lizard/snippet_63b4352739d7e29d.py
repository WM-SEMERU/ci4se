def export(self, nidm_version, export_dir):
    self.add_attributes(((PROV['type'], self.type), (
        NIDM_IN_COORDINATE_SPACE, self.coord_space.id), (PROV['label'],
        self.label)))
    if self.visu is not None:
        self.add_attributes(((DC['description'], self.visu.id),))
    if self.clust_map is not None:
        self.add_attributes(((NIDM_HAS_CLUSTER_LABELS_MAP, self.clust_map.id),)
            )
    if self.mip is not None:
        self.add_attributes(((NIDM_HAS_MAXIMUM_INTENSITY_PROJECTION, self.
            mip.id),))
    if self.num_clusters is not None:
        self.add_attributes(((NIDM_NUMBER_OF_CLUSTERS, self.num_clusters),))
    if self.p_value is not None:
        self.add_attributes(((NIDM_P_VALUE, self.p_value),))