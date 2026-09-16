def main_browse():
    parser = argparse.ArgumentParser(usage='job_archive.py [options]',
        description='Browse a job archive')
    parser.add_argument('--jobs', action='store', dest='job_archive_table',
        type=str, default='job_archive_temp2.fits', help='Job archive file')
    parser.add_argument('--files', action='store', dest=
        'file_archive_table', type=str, default='file_archive_temp2.fits',
        help='File archive file')
    parser.add_argument('--base', action='store', dest='base_path', type=
        str, default=os.path.abspath('.'), help='File archive base path')
    args = parser.parse_args(sys.argv[1:])
    job_ar = JobArchive.build_archive(**args.__dict__)
    job_ar.table.pprint()