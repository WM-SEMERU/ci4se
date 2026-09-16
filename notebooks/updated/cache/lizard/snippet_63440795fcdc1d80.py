def return_single_path_base(dbpath, set_object, object_id):
    engine = create_engine('sqlite:////' + dbpath)
    session_cl = sessionmaker(bind=engine)
    session = session_cl()
    tmp_object = session.query(set_object).get(object_id)
    session.close()
    return tmp_object.path