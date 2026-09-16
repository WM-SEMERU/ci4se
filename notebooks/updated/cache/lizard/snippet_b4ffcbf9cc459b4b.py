def get_last_traded_dt(self, asset, dt):
    sid_ix = self.sids.searchsorted(asset.sid)
    dt_limit_ix = self.dates.searchsorted(dt.asm8, side='right')
    nonzero_volume_ixs = np.ravel(np.nonzero(self._country_group[DATA][
        VOLUME][(sid_ix), :dt_limit_ix]))
    if len(nonzero_volume_ixs) == 0:
        return pd.NaT
    return pd.Timestamp(self.dates[nonzero_volume_ixs][-1], tz='UTC')