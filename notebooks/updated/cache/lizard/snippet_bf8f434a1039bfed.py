def write_catalogue(self, output_file, key_list=SORTED_ATTRIBUTE_LIST):
    with open(output_file, 'w') as of:
        writer = csv.DictWriter(of, fieldnames=key_list)
        writer.writeheader()
        for i in range(self.get_number_events()):
            row_dict = {}
            for key in key_list:
                if len(self.data[key]) > 0:
                    data = self.data[key][i]
                    if key in self.INT_ATTRIBUTE_LIST:
                        if np.isnan(data):
                            data = ''
                        else:
                            data = int(data)
                    if key in self.FLOAT_ATTRIBUTE_LIST:
                        if np.isnan(data):
                            data = ''
                        else:
                            data = float(data)
                row_dict[key] = data
            writer.writerow(row_dict)