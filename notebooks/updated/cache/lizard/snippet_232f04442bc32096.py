def load_pickle(filename):
    try:
        if pd:
            return pd.read_pickle(filename), None
        else:
            with open(filename, 'rb') as fid:
                data = pickle.load(fid)
            return data, None
    except Exception as err:
        return None, str(err)