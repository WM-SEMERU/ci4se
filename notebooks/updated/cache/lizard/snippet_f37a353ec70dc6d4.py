def Q_stock(self):
    return self._Q_sys * (self._C_sys / self._C_stock).to(u.dimensionless)