def over(self, window):
    from pyspark.sql.window import WindowSpec
    if not isinstance(window, WindowSpec):
        raise TypeError('window should be WindowSpec')
    jc = self._jc.over(window._jspec)
    return Column(jc)