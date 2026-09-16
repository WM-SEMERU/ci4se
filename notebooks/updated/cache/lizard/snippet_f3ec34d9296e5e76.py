def _encode_dict(d):

    def enc(x):
        if isinstance(x, six.text_type):
            return x.encode(_ENCODING)
        else:
            return x
    return dict((enc(k), enc(v)) for k, v in six.iteritems(d))