def QA_SU_save_stock_min(engine, client=DATABASE):
    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_min(client=client)