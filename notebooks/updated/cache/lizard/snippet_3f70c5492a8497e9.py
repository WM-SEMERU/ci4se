def convert_characteristicFaultSource(self, node):
    char = source.CharacteristicFaultSource(source_id=node['id'], name=node
        ['name'], tectonic_region_type=node.attrib.get('tectonicRegion'),
        mfd=self.convert_mfdist(node), surface=self.convert_surfaces(node.
        surface), rake=~node.rake, temporal_occurrence_model=self.get_tom(node)
        )
    return char