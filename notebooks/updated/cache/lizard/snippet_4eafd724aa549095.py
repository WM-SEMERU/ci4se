def fill_from_allwise(self, ident, catalog_ident='II/328/allwise'):
    from astroquery.vizier import Vizier
    import numpy.ma.core as ma_core
    table_list = Vizier.query_constraints(catalog=catalog_ident, AllWISE=ident)
    if not len(table_list):
        raise PKError('Vizier query returned no tables (catalog=%r AllWISE=%r)'
            , catalog_ident, ident)
    table = table_list[0]
    if not len(table):
        raise PKError(
            'Vizier query returned empty %s table (catalog=%r AllWISE=%r)',
            table.meta['name'], catalog_ident, ident)
    row = table[0]
    if isinstance(row['_RAJ2000'], ma_core.MaskedConstant):
        raise PKError(
            'Vizier query returned flagged row in %s table; your AllWISE identifier likely does not exist (it should be of the form "J112254.70+255021.9"; catalog=%r AllWISE=%r)'
            , table.meta['name'], catalog_ident, ident)
    self.ra = row['RA_pm'] * D2R
    self.dec = row['DE_pm'] * D2R
    if row['e_RA_pm'] > row['e_DE_pm']:
        self.pos_u_maj = row['e_RA_pm'] * A2R
        self.pos_u_min = row['e_DE_pm'] * A2R
        self.pos_u_pa = halfpi
    else:
        self.pos_u_maj = row['e_DE_pm'] * A2R
        self.pos_u_min = row['e_RA_pm'] * A2R
        self.pos_u_pa = 0
    self.pos_epoch = 55400.0
    self.promo_ra = row['pmRA']
    self.promo_dec = row['pmDE']
    if row['e_pmRA'] > row['e_pmDE']:
        self.promo_u_maj = row['e_pmRA'] * 1.0
        self.promo_u_min = row['e_pmDE'] * 1.0
        self.promo_u_pa = halfpi
    else:
        self.promo_u_maj = row['e_pmDE'] * 1.0
        self.promo_u_min = row['e_pmRA'] * 1.0
        self.promo_u_pa = 0.0
    return self