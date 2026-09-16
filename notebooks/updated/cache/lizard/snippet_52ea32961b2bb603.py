def model_select(self, score_function, alleles=None, min_models=1,
    max_models=10000):
    if alleles is None:
        alleles = self.supported_alleles
    dfs = []
    allele_to_allele_specific_models = {}
    for allele in alleles:
        df = pandas.DataFrame({'model': self.
            allele_to_allele_specific_models[allele]})
        df['model_num'] = df.index
        df['allele'] = allele
        df['selected'] = False
        round_num = 1
        while not df.selected.all() and sum(df.selected) < max_models:
            score_col = 'score_%2d' % round_num
            prev_score_col = 'score_%2d' % (round_num - 1)
            existing_selected = list(df[df.selected].model)
            df[score_col] = [(numpy.nan if row.selected else score_function
                (Class1AffinityPredictor(allele_to_allele_specific_models={
                allele: [row.model] + existing_selected}))) for _, row in
                df.iterrows()]
            if round_num > min_models and df[score_col].max() < df[
                prev_score_col].max():
                break
            best_model_index, = df.loc[df[score_col] == df[score_col].max()
                ].sample(1).index
            df.loc[best_model_index, 'selected'] = True
            round_num += 1
        dfs.append(df)
        allele_to_allele_specific_models[allele] = list(df.loc[df.selected]
            .model)
    df = pandas.concat(dfs, ignore_index=True)
    new_predictor = Class1AffinityPredictor(allele_to_allele_specific_models,
        metadata_dataframes={'model_selection': df})
    return new_predictor