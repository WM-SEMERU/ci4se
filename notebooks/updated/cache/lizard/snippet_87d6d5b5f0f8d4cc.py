def check_dataframe(self, dataframe):
    required_columns = 'a', 'b', 'm', 'n', 'r'
    for column in required_columns:
        if column not in dataframe:
            raise Exception('Required column not in dataframe: {0}'.format(
                column))