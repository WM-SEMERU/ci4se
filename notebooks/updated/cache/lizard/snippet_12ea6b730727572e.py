def annotation_spec_path(cls, project, location, dataset, annotation_spec):
    return google.api_core.path_template.expand(
        'projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}'
        , project=project, location=location, dataset=dataset,
        annotation_spec=annotation_spec)