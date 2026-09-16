def _add_products(self, tile, show_all=False):
    products = tile.products
    unique_id = tile.unique_id
    base_path = tile.output_folder
    for prod_path, prod_type in products.items():
        if (prod_path == 'tilebus_definitions' or prod_path ==
            'include_directories'):
            continue
        if prod_type in self.IGNORED_PRODUCTS:
            continue
        prod_base = os.path.basename(prod_path)
        if prod_type not in self._product_map:
            self._product_map[prod_type] = {}
        prod_map = self._product_map[prod_type]
        if prod_base not in prod_map:
            prod_map[prod_base] = []
        full_path = os.path.normpath(os.path.join(base_path, prod_path))
        info = ProductInfo(prod_base, full_path, unique_id, not show_all and
            prod_base not in self._product_filter)
        prod_map[prod_base].append(info)