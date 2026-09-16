def get_resource_children(raml_resource):
    path = raml_resource.path
    return [res for res in raml_resource.root.resources if res.parent and 
        res.parent.path == path]