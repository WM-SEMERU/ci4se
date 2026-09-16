def merge_sources(self, datas):
    datas = [data for data in datas if data is not None]
    if len(datas) == 0:
        raise ValueError('Data missing')
    if len(datas) == 1:
        return datas[0]
    if isinstance(datas[0], list):
        if len([x for x in datas if not isinstance(x, list)]) > 0:
            raise TypeError('Unable to merge: List expected')
        base = []
        for x in datas:
            base = base + x
        return base
    if isinstance(datas[0], dict):
        if len([x for x in datas if not isinstance(x, dict)]) > 0:
            raise TypeError('Unable to merge: Dictionnary expected')
        result = {}
        for element in datas:
            for key in element:
                if key in result:
                    result[key] = self.merge_sources([result[key], element[
                        key]])
                else:
                    result[key] = element[key]
        return result
    if len([x for x in datas if isinstance(x, (dict, list))]) > 0:
        raise TypeError('Unable to merge: List not expected')
    raise ValueError('Unable to merge: Conflict')