def QA_SU_save_etf_list(client=DATABASE, ui_log=None, ui_progress=None):
    try:
        QA_util_log_info('##JOB16 Now Saving ETF_LIST ====', ui_log=ui_log,
            ui_progress=ui_progress, ui_progress_int_value=5000)
        etf_list_from_tdx = QA_fetch_get_stock_list(type_='etf')
        pandas_data = QA_util_to_json_from_pandas(etf_list_from_tdx)
        if len(pandas_data) > 0:
            client.drop_collection('etf_list')
            coll = client.etf_list
            coll.create_index('code')
            coll.insert_many(pandas_data)
        QA_util_log_info('完成ETF列表获取', ui_log=ui_log, ui_progress=
            ui_progress, ui_progress_int_value=10000)
    except Exception as e:
        QA_util_log_info(e, ui_log=ui_log)
        print(' Error save_tdx.QA_SU_save_etf_list exception!')
        pass