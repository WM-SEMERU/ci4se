def product_set_path(cls, project, location, product_set):
    return google.api_core.path_template.expand(
        'projects/{project}/locations/{location}/productSets/{product_set}',
        project=project, location=location, product_set=product_set)