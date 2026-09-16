def items_with_price(raw_df):
    df = raw_df[['PRONAC', 'idPlanilhaAprovacao', 'Item', 'idPlanilhaItens',
        'VlUnitarioAprovado', 'idSegmento', 'DataProjeto', 'idPronac',
        'UfItem', 'idProduto', 'cdCidade', 'cdEtapa']].copy()
    df['VlUnitarioAprovado'] = df['VlUnitarioAprovado'].apply(pd.to_numeric)
    return df