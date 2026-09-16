def get_file_from_gdc(job, gdc_url, gdc_download_token, write_to_jobstore=True
    ):
    work_dir = job.fileStore.getLocalTempDir()
    parsed_url = urlparse(gdc_url)
    assert parsed_url.scheme == 'gdc', 'Unexpected url scheme: %s' % gdc_url
    file_dir = '/'.join([work_dir, parsed_url.netloc])
    currwd = os.getcwd()
    os.chdir(work_dir)
    try:
        download_call = ['gdc-client', 'download', '-t', gdc_download_token,
            parsed_url.netloc]
        subprocess.check_call(download_call)
    finally:
        os.chdir(currwd)
    assert os.path.exists(file_dir)
    output_files = [os.path.join(file_dir, x) for x in os.listdir(file_dir) if
        not x.endswith('logs')]
    if len(output_files) == 1:
        assert output_files[0].endswith('vcf')
    else:
        if not {os.path.splitext(x)[1] for x in output_files} >= {'.bam',
            '.bai'}:
            raise ParameterError(
                'Can currently only handle pre-indexed GDC bams.')
        output_files = [x for x in output_files if x.endswith(('bam', 'bai'))]
        output_files = sorted(output_files, key=lambda x: os.path.splitext(
            x)[1], reverse=True)
    if write_to_jobstore:
        output_files = [job.fileStore.writeGlobalFile(f) for f in output_files]
    return output_files