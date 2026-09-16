def review_metadata_csv(filedir, input_filepath):
    try:
        metadata = load_metadata_csv(input_filepath)
    except ValueError as e:
        print_error(e)
        return False
    with open(input_filepath) as f:
        csv_in = csv.reader(f)
        header = next(csv_in)
        n_headers = len(header)
        if header[0] == 'filename':
            res = review_metadata_csv_single_user(filedir, metadata, csv_in,
                n_headers)
            return res
        if header[0] == 'project_member_id':
            res = review_metadata_csv_multi_user(filedir, metadata, csv_in,
                n_headers)
            return res