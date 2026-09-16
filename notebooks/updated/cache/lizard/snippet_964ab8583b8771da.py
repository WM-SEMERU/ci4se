def ebi_expression_atlas(accession: str, *, filter_boring: bool=False):
    experiment_dir = settings.datasetdir / accession
    dataset_path = experiment_dir / '{}.h5ad'.format(accession)
    try:
        adata = anndata.read(dataset_path)
        if filter_boring:
            adata.obs = _filter_boring(adata.obs)
        return adata
    except OSError:
        pass
    download_experiment(accession)
    print('Downloaded {} to {}'.format(accession, experiment_dir.absolute()))
    with ZipFile(experiment_dir / 'expression_archive.zip', 'r') as f:
        adata = read_expression_from_archive(f)
    obs = pd.read_csv(experiment_dir / 'experimental_design.tsv', sep='\t',
        index_col=0)
    adata.obs[obs.columns] = obs
    adata.write(dataset_path, compression='gzip')
    if filter_boring:
        adata.obs = _filter_boring(adata.obs)
    return adata