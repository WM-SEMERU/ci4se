def add_colors_from_file(self, system, f_or_filename):
    if hasattr(f_or_filename, 'read'):
        colors = (row for row in csv.reader(f_or_filename) if row)
    else:
        with open(f_or_filename, 'rb') as f:
            colors = [row for row in csv.reader(f) if row]
    self.add_colors(system, colors)