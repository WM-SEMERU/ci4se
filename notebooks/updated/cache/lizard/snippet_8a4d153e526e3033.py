def footprint(self):
    product_footprint = self._product_metadata.iter('Product_Footprint')
    for element in product_footprint:
        global_footprint = None
        for global_footprint in element.iter('Global_Footprint'):
            coords = global_footprint.findtext('EXT_POS_LIST').split()
            return _polygon_from_coords(coords)