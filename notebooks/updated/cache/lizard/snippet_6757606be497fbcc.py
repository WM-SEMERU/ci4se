def has_layer(fcollection):
    for val in six.viewvalues(fcollection):
        if has_features(val):
            return True
    return False