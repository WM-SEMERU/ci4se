def write_phosphopath(df, f, extra_columns=None):
    proteins = [_protein_id(k) for k in df.index.get_level_values('Proteins')]
    amino_acids = df.index.get_level_values('Amino acid')
    positions = _get_positions(df)
    multiplicity = [k[-1] for k in df.index.get_level_values('Multiplicity')]
    apos = [('%s%s' % x) for x in zip(amino_acids, positions)]
    prar = [('%s-%s' % x) for x in zip(proteins, apos)]
    phdf = pd.DataFrame(np.array(list(zip(proteins, prar, apos, multiplicity)))
        )
    if extra_columns:
        for c in extra_columns:
            phdf[c] = df[c].values
    phdf.to_csv(f, sep='\t', index=None, header=None)