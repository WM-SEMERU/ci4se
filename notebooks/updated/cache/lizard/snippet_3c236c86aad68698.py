def build_data_table(energy, flux, flux_error=None, flux_error_lo=None,
    flux_error_hi=None, energy_width=None, energy_lo=None, energy_hi=None,
    ul=None, cl=None):
    table = QTable()
    if cl is not None:
        cl = validate_scalar('cl', cl)
        table.meta['keywords'] = {'cl': {'value': cl}}
    table['energy'] = energy
    if energy_width is not None:
        table['energy_width'] = energy_width
    elif energy_lo is not None and energy_hi is not None:
        table['energy_lo'] = energy_lo
        table['energy_hi'] = energy_hi
    table['flux'] = flux
    if flux_error is not None:
        table['flux_error'] = flux_error
    elif flux_error_lo is not None and flux_error_hi is not None:
        table['flux_error_lo'] = flux_error_lo
        table['flux_error_hi'] = flux_error_hi
    else:
        raise TypeError('Flux error not provided!')
    if ul is not None:
        ul = np.array(ul, dtype=np.int)
        table['ul'] = ul
    table.meta['comments'] = ['Table generated with naima.build_data_table']
    validate_data_table(table)
    return table