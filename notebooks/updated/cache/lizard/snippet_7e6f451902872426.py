def __get_data_en_intervalo(self, d0=None, df=None):
    params = {'date_fmt': self.DATE_FMT, 'usar_multithread': self.
        USAR_MULTITHREAD, 'max_threads_requests': self.MAX_THREADS_REQUESTS,
        'timeout': self.TIMEOUT, 'num_retries': self.NUM_RETRIES,
        'func_procesa_data_dia': self.procesa_data_dia, 'func_url_data_dia':
        self.url_data_dia, 'max_act_exec': self.MAX_ACT_EXEC,
        'data_extra_request': {'headers': self.HEADERS, 'json_req': self.
        JSON_REQUESTS, 'params_request': self.PARAMS_REQUESTS}, 'verbose':
        self.verbose}
    data_get, hay_errores, str_import = get_data_en_intervalo(d0, df, **params)
    if not hay_errores:
        self.integridad_data(data_get)
        self.printif(str_import, 'ok')
        if type(data_get) is pd.DataFrame:
            data_get = {self.masterkey: data_get}
        return data_get
    else:
        return None