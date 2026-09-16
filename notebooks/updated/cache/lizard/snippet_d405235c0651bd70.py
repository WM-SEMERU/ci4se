def _map_arguments(self, args):
    config_yaml = args['config']
    config_dict = load_yaml(config_yaml)
    dry_run = args.get('dry_run', False)
    data = config_dict.get('data')
    comp = config_dict.get('comp')
    library = config_dict.get('library')
    models = config_dict.get('models')
    scratch = config_dict.get('scratch')
    self._set_link('prepare', SplitAndBinChain, comp=comp, data=data,
        ft1file=config_dict.get('ft1file'), hpx_order_ccube=config_dict.get
        ('hpx_order_ccube'), hpx_order_expcube=config_dict.get(
        'hpx_order_expcube'), scratch=scratch, dry_run=dry_run)
    self._set_link('diffuse-comp', DiffuseCompChain, comp=comp, data=data,
        library=library, make_xml=config_dict.get('make_diffuse_comp_xml',
        False), outdir=config_dict.get('merged_gasmap_dir', 'merged_gasmap'
        ), dry_run=dry_run)
    self._set_link('catalog-comp', CatalogCompChain, comp=comp, data=data,
        library=library, make_xml=config_dict.get('make_catalog_comp_xml',
        False), nsrc=config_dict.get('catalog_nsrc', 500), dry_run=dry_run)
    self._set_link('assemble-model', AssembleModelChain, comp=comp, data=
        data, library=library, models=models, hpx_order=config_dict.get(
        'hpx_order_fitting'), dry_run=dry_run)