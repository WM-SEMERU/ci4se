def generate_contour_data(pid):
    if isinstance(pid, GenInput):
        pid = pid.return_dict()
    begin_time = time.time()
    WORKING_DIRECTORY = '.'
    if 'WORKING_DIRECTORY' not in pid['general'].keys():
        pid['general']['WORKING_DIRECTORY'] = WORKING_DIRECTORY
    running_process = GenProcess(**{**pid, **pid['generate_info']})
    running_process.set_parameters()
    running_process.run_snr()
    file_out = FileReadOut(running_process.xvals, running_process.yvals,
        running_process.final_dict, **{**pid['general'], **pid[
        'generate_info'], **pid['output_info']})
    print('outputing file:', pid['general']['WORKING_DIRECTORY'] + '/' +
        pid['output_info']['output_file_name'])
    getattr(file_out, file_out.output_file_type + '_read_out')()
    print(time.time() - begin_time)
    return