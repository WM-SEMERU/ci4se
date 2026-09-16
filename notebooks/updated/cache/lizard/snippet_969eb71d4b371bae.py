def iter_python_modules(tile):
    for product_type in tile.PYTHON_PRODUCTS:
        for product in tile.find_products(product_type):
            entry_point = ENTRY_POINT_MAP.get(product_type)
            if entry_point is None:
                raise BuildError(
                    'Found an unknown python product (%s) whose entrypoint could not be determined (%s)'
                     % (product_type, product))
            if ':' in product:
                module, _, obj_name = product.rpartition(':')
            else:
                module = product
                obj_name = None
            if not os.path.exists(module):
                raise BuildError(
                    'Found a python product whose path did not exist: %s' %
                    module)
            product_name = os.path.basename(module)
            if product_name.endswith('.py'):
                product_name = product_name[:-3]
            import_string = '{} = {}.{}'.format(product_name, tile.
                support_distribution, product_name)
            if obj_name is not None:
                import_string += ':{}'.format(obj_name)
            yield module, import_string, entry_point