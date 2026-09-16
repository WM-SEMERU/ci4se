def upload_sequence_fileobj(file_obj, file_name, fields, retry_fields,
    session, samples_resource):
    try:
        _direct_upload(file_obj, file_name, fields, session, samples_resource)
        sample_id = fields['sample_id']
    except RetryableUploadException:
        logging.error('{}: Connectivity issue, trying direct upload...'.
            format(file_name))
        file_obj.seek(0)
        try:
            retry_fields = samples_resource.init_multipart_upload(retry_fields)
        except requests.exceptions.HTTPError as e:
            raise_api_error(e.response, state='init')
        except requests.exceptions.ConnectionError:
            raise_connectivity_error(file_name)
        s3_upload = _s3_intermediate_upload(file_obj, file_name,
            retry_fields, session, samples_resource._client._root_url +
            retry_fields['callback_url'])
        sample_id = s3_upload.get('sample_id', '<UUID not yet assigned>')
    logging.info('{}: finished as sample {}'.format(file_name, sample_id))
    return sample_id