def load_user_catalog():
    cat_dir = user_data_dir()
    if not os.path.isdir(cat_dir):
        return Catalog()
    else:
        return YAMLFilesCatalog(cat_dir)