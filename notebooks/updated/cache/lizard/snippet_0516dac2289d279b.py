def save(self, filename):
    f = open(filename, mode='w')
    for p in self.rally_points:
        f.write('RALLY %f\t%f\t%f\t%f\t%f\t%d\n' % (p.lat * 1e-07, p.lng * 
            1e-07, p.alt, p.break_alt, p.land_dir, p.flags))
    f.close()