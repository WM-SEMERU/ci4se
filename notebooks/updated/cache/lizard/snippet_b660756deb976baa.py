def read_data(self, scaling_factor=1e-09, strain_headers=None):
    if strain_headers:
        self.strain.data_variables = strain_headers
    else:
        self.strain.data_variables = STRAIN_VARIABLES
    datafile = open(self.filename, 'r')
    reader = csv.DictReader(datafile)
    self.strain.data = dict([(name, []) for name in reader.fieldnames])
    for row in reader:
        for name in row.keys():
            if 'region' in name.lower():
                self.strain.data[name].append(row[name])
            elif name in self.strain.data_variables:
                self.strain.data[name].append(scaling_factor * float(row[name])
                    )
            else:
                self.strain.data[name].append(float(row[name]))
    for key in self.strain.data.keys():
        if 'region' in key:
            self.strain.data[key] = np.array(self.strain.data[key], dtype='S13'
                )
        else:
            self.strain.data[key] = np.array(self.strain.data[key])
    self._check_invalid_longitudes()
    if 'region' not in self.strain.data:
        print('No tectonic regionalisation found in input file!')
    self.strain.data_variables = self.strain.data.keys()
    self.strain.get_secondary_strain_data()
    return self.strain