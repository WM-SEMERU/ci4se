def _rehydrate_skeleton_class(skeleton_class, class_dict):
    for attrname, attr in class_dict.items():
        setattr(skeleton_class, attrname, attr)
    return skeleton_class