def load_metadata_csv(input_filepath):
    with open(input_filepath) as f:
        csv_in = csv.reader(f)
        header = next(csv_in)
        if 'tags' in header:
            tags_idx = header.index('tags')
        else:
            raise ValueError('"tags" is a compulsory column in metadata file.')
        if header[0] == 'project_member_id':
            if header[1] == 'filename':
                metadata = load_metadata_csv_multi_user(csv_in, header,
                    tags_idx)
            else:
                raise ValueError('The second column must be "filename"')
        elif header[0] == 'filename':
            metadata = load_metadata_csv_single_user(csv_in, header, tags_idx)
        else:
            raise ValueError('Incorrect Formatting of metadata. The first' +
                ' column for single user upload should be' +
                ' "filename". For multiuser uploads the first ' +
                'column should be "project member id" and the' +
                ' second column should be "filename"')
    return metadata