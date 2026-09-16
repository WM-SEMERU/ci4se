def _revert_caffe2_pad(attr):
    if len(attr) == 4:
        attr = attr[:2]
    elif len(attr) == 2:
        pass
    else:
        raise ValueError('Invalid caffe2 type padding: {}'.format(attr))
    return attr