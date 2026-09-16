def add_col_features(self, col=None, degree=None):
    if not col and not degree:
        return
    elif isinstance(col, list) and isinstance(degree, list):
        if len(col) != len(degree):
            print('col len: ', len(col))
            print('degree len: ', len(degree))
            raise ValueError('col and degree should have equal length.')
        else:
            if self.preprocessed_data.empty:
                data = self.original_data
            else:
                data = self.preprocessed_data
            for i in range(len(col)):
                data.loc[:, (col[i] + str(degree[i]))] = pow(data.loc[:, (
                    col[i])], degree[i]) / pow(10, degree[i] - 1)
            self.preprocessed_data = data
    else:
        raise TypeError('col and degree should be lists.')