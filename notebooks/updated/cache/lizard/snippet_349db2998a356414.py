def insert_data_point(self, new_data, index=None):
    if not len(new_data) == len(self.columns) and not len(self.columns) == 0:
        print(
            'ERROR: new_data must have as many elements as there are columns.')
        return
    elif len(self.columns) == 0:
        for i in range(len(new_data)):
            self[i] = [new_data[i]]
    else:
        for i in range(len(new_data)):
            data = list(self[i])
            if index is None:
                data.append(new_data[i])
            else:
                data.insert(index, new_data[i])
            self[i] = _n.array(data)
    return self