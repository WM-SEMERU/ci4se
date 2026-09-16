def build_strain_specific_models(self, save_models=False):
    if len(self.df_orthology_matrix) == 0:
        raise RuntimeError('Empty orthology matrix')
    for strain_gempro in tqdm(self.strains):
        log.debug('{}: building strain specific model'.format(strain_gempro.id)
            )
        logging.disable(logging.WARNING)
        if self._empty_reference_gempro.model:
            strain_gempro.load_cobra_model(self._empty_reference_gempro.model)
        elif self._empty_reference_gempro.genes:
            strain_gempro.genes = [x.id for x in self.
                _empty_reference_gempro.genes]
        logging.disable(logging.NOTSET)
        not_in_strain = self.df_orthology_matrix[pd.isnull(self.
            df_orthology_matrix[strain_gempro.id])][strain_gempro.id
            ].index.tolist()
        self._pare_down_model(strain_gempro=strain_gempro, genes_to_remove=
            not_in_strain)
        self._load_strain_sequences(strain_gempro=strain_gempro)
        if save_models:
            cobra.io.save_json_model(model=strain_gempro.model, filename=op
                .join(self.model_dir, '{}.json'.format(strain_gempro.id)))
            strain_gempro.save_pickle(op.join(self.model_dir, '{}_gp.pckl'.
                format(strain_gempro.id)))
    log.info('Created {} new strain-specific models and loaded in sequences'
        .format(len(self.strains)))