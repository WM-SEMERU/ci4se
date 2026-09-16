def get_column_labels(obj):
    if not isinstance(obj, (list, tuple, pd.np.ndarray)):
        try:
            labels = [f.name for f in obj.model._meta.fields]
        except:
            try:
                labels = obj.keys()
            except:
                try:
                    labels = dir(obj)
                except:
                    labels = None
    elif all(isinstance(heading, basestring) for heading in obj[0]):
        labels = list(obj[0])
        del obj[0]
    return labels