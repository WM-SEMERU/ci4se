def write(self, equities=None, futures=None, exchanges=None, root_symbols=
    None, equity_supplementary_mappings=None, chunk_size=DEFAULT_CHUNK_SIZE):
    if exchanges is None:
        exchange_names = [df['exchange'] for df in (equities, futures,
            root_symbols) if df is not None]
        if exchange_names:
            exchanges = pd.DataFrame({'exchange': pd.concat(exchange_names)
                .unique()})
    data = self._load_data(equities if equities is not None else pd.
        DataFrame(), futures if futures is not None else pd.DataFrame(), 
        exchanges if exchanges is not None else pd.DataFrame(), 
        root_symbols if root_symbols is not None else pd.DataFrame(), 
        equity_supplementary_mappings if equity_supplementary_mappings is not
        None else pd.DataFrame())
    self._real_write(equities=data.equities, equity_symbol_mappings=data.
        equities_mappings, equity_supplementary_mappings=data.
        equity_supplementary_mappings, futures=data.futures, root_symbols=
        data.root_symbols, exchanges=data.exchanges, chunk_size=chunk_size)