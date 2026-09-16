def get_annotation(db_path, db_list):
    annotated = False
    for db in db_list:
        if db['path'] == db_path:
            annotated = db['annotated']
            break
    return annotated