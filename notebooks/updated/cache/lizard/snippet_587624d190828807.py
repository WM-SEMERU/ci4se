def new(arg_name, annotated_with=None):
    if annotated_with is not None:
        annotation = annotations.Annotation(annotated_with)
    else:
        annotation = annotations.NO_ANNOTATION
    return BindingKey(arg_name, annotation)