def make_gtf_filename(ensembl_release, species):
    ensembl_release, species, reference_name = normalize_release_properties(
        ensembl_release, species)
    return GTF_FILENAME_TEMPLATE % {'Species': species.capitalize(),
        'reference': reference_name, 'release': ensembl_release}