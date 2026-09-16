def convert_nexus_to_format(dataset_as_nexus, dataset_format):
    fake_handle = StringIO(dataset_as_nexus)
    nexus_al = AlignIO.parse(fake_handle, 'nexus')
    tmp_file = make_random_filename()
    AlignIO.write(nexus_al, tmp_file, dataset_format)
    dataset_as_fasta = read_and_delete_tmp_file(tmp_file)
    return dataset_as_fasta