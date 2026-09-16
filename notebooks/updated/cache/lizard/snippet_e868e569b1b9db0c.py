def export_to_bw2(self):
    my_exporter = Bw2Exporter(self)
    name, bw2db = my_exporter.export_to_bw2()
    return name, bw2db