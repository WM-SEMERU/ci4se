def how_similar_dicts(dict1, dict2):
    values = []
    for k in dict1:
        if k in dict2 and dict1[k] and dict2[k]:
            values.append(how_similar_are(str(dict1[k]), str(dict2[k])))
    return np.mean(values)