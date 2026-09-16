def get_output_content(job_id, max_size=1024, conn=None):
    content = None
    if RBO.index_list().contains(IDX_OUTPUT_JOB_ID).run(conn):
        check_status = RBO.get_all(job_id, index=IDX_OUTPUT_JOB_ID).run(conn)
    else:
        check_status = RBO.filter({OUTPUTJOB_FIELD: {ID_FIELD: job_id}}).run(
            conn)
    for status_item in check_status:
        content = _truncate_output_content_if_required(status_item, max_size)
    return content