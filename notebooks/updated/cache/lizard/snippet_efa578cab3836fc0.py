def fhs2data_combo(fhs, cols, index, labels=None, col_sep=': '):
    if labels is None:
        labels = [basename(fh) for fh in fhs]
    if len(fhs) > 0:
        for fhi, fh in enumerate(fhs):
            label = labels[fhi]
            data = pd.read_csv(fh).set_index(index)
            if fhi == 0:
                data_combo = pd.DataFrame(index=data.index)
                for col in cols:
                    data_combo.loc[:, ('%s%s%s' % (label, col_sep, col))
                        ] = data.loc[:, (col)]
            else:
                for col in cols:
                    data_combo.loc[:, ('%s%s%s' % (label, col_sep, col))
                        ] = data.loc[:, (col)]
        return data_combo
    else:
        logging.error('no fhs found: len(fhs)=0')