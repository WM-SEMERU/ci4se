def deepcopy(data):
    try:
        return pickle.loads(pickle.dumps(data))
    except TypeError:
        return copy.deepcopy(data)