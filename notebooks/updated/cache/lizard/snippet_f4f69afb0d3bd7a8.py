def read_in_weight_table(self, in_weight_table):
    print('Reading the weight table...')
    with open_csv(in_weight_table, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header_row = next(reader)
        if len(header_row) < len(self.header_wt):
            raise Exception(self.error_messages[4])
        if header_row[1:len(self.header_wt)] != self.header_wt[1:]:
            raise Exception(self.error_messages[5])
    self.dict_list = np.loadtxt(in_weight_table, delimiter=',', usecols=(0,
        1, 2, 3, 4), skiprows=1, dtype={'names': (self.header_wt[0], self.
        header_wt[1], self.header_wt[2], self.header_wt[3], self.header_wt[
        4]), 'formats': ('i8', 'f8', 'i8', 'i8', 'i8')})
    self.count = self.dict_list.shape[0]
    self.size_stream_id = len(np.unique(np.array(self.dict_list[self.
        header_wt[0]], dtype=np.int32)))