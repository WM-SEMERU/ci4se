def write_tsv(self, path):
    with open(path, 'wb') as ofh:
        writer = csv.writer(ofh, dialect='excel-tab', quoting=csv.
            QUOTE_NONE, lineterminator=os.linesep)
        for gs in self._gene_sets.values():
            writer.writerow(gs.to_list())