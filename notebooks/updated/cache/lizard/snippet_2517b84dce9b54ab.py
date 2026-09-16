def add_summary_page(self):
    s = PortfolioSummary()
    s.include_long_short()
    pieces = []
    for r in self.results:
        tmp = s(r.port, PortfolioSummary.analyze_returns)
        tmp['desc'] = r.desc
        tmp['sid'] = r.sid
        tmp = tmp.set_index(['sid', 'desc'], append=1).reorder_levels([2, 1, 0]
            )
        pieces.append(tmp)
    frame = pd.concat(pieces)
    tf = self.pdf.table_formatter(frame)
    tf.apply_basic_style(cmap=self.table_style)
    tf.cells.match_column_labels(['nmonths', 'cnt', 'win cnt', 'lose cnt',
        'dur max']).int_format()
    tf.cells.match_column_labels(['sharpe ann', 'sortino', 'dur avg']
        ).float_format(precision=1)
    tf.cells.match_column_labels(['maxdd dt']).apply_format(
        new_datetime_formatter('%d-%b-%y'))
    tf.cells.match_column_labels(['cagr', 'mret avg', 'mret std ann',
        'ret std', 'mret avg ann', 'maxdd', 'avg dd', 'winpct', 'ret avg',
        'ret min', 'ret max']).percent_format()
    self.pdf.build_page('summary', {'F1': tf.build()})