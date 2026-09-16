def write_electrodes(self, filename):
    fid = open(filename, 'w')
    for i in self.Electrodes:
        fid.write('{0} {1}\n'.format(self.Points[i][0], self.Points[i][1]))
    fid.close()