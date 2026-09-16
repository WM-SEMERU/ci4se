def buy_and_hold(self, qty=1.0, start_dt=None, end_dt=None, start_px=None,
    end_px=None):
    from tia.analysis.model.trd import TradeBlotter
    eod = self.pricer.get_eod_frame().close
    start_dt = start_dt and pd.to_datetime(start_dt) or eod.index[0]
    start_px = start_px or eod.asof(start_dt)
    end_dt = end_dt and pd.to_datetime(end_dt) or eod.index[-1]
    end_px = end_px or eod.asof(end_dt)
    pricer = self.pricer.trunace(start_dt, end_dt)
    blotter = TradeBlotter()
    blotter.ts = start_dt
    blotter.open(qty, start_px)
    blotter.ts = end_dt
    blotter.close(end_px)
    trds = blotter.trades
    return SingleAssetPortfolio(pricer, trds, ret_calc=self.ret_calc)