def dict_setdiff(dict_, negative_keys):
    r
    keys = [key for key in six.iterkeys(dict_) if key not in set(negative_keys)
        ]
    subdict_ = dict_subset(dict_, keys)
    return subdict_