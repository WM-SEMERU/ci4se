def score_genes_cell_cycle(adata, s_genes, g2m_genes, copy=False, **kwargs):
    logg.info('calculating cell cycle phase')
    adata = adata.copy() if copy else adata
    ctrl_size = min(len(s_genes), len(g2m_genes))
    score_genes(adata, gene_list=s_genes, score_name='S_score', ctrl_size=
        ctrl_size, **kwargs)
    score_genes(adata, gene_list=g2m_genes, score_name='G2M_score',
        ctrl_size=ctrl_size, **kwargs)
    scores = adata.obs[['S_score', 'G2M_score']]
    phase = pd.Series('S', index=scores.index)
    phase[scores.G2M_score > scores.S_score] = 'G2M'
    phase[np.all(scores < 0, axis=1)] = 'G1'
    adata.obs['phase'] = phase
    logg.hint("    'phase', cell cycle phase (adata.obs)")
    return adata if copy else None