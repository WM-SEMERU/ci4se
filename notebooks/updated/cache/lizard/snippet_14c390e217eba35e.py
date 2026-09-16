def write_sample_sheet(path, accessions, names, celfile_urls, sel=None):
    with open(path, 'wb') as ofh:
        writer = csv.writer(ofh, dialect='excel-tab', lineterminator=os.
            linesep, quoting=csv.QUOTE_NONE)
        writer.writerow(['Accession', 'Name', 'CEL file', 'CEL file URL'])
        n = len(names)
        if sel is None:
            sel = range(n)
        for i in sel:
            cf = celfile_urls[i].split('/')[-1]
            writer.writerow([accessions[i], names[i], cf, celfile_urls[i]])