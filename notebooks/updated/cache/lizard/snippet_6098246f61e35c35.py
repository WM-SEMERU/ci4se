def get_features_from_equation(container_dir, product_name):
    import featuremonkey
    file_path = os.path.join(container_dir, 'products', product_name,
        'product.equation')
    return featuremonkey.get_features_from_equation_file(file_path)