def add_annotations(self, annotations, **kwargs):
    ann_kwargs = utils.check_kwargs(kwargs, get_annotation_kwargs(), {},
        clean_origin=True)
    if type(annotations) == list:
        self.layout['annotations']['values'].extend(annotations)
    else:
        self.layout['annotations']['values'].append(annotations)
    if ann_kwargs:
        self.layout['annotations']['params'].update(**ann_kwargs)