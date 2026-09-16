def generate_jobs(args, job_list, argument_string):
    mvtest_path = args.mvpath
    template = ''.join(args.template.readlines())
    logpath = os.path.abspath(args.logpath)
    respath = os.path.abspath(args.res_path)
    scriptpath = os.path.abspath(args.script_path)
    pwd = os.path.abspath(os.getcwd())
    for jobname in job_list.keys():
        filename = '%s/%s.sh' % (scriptpath, jobname)
        job_body = mvtest_path + ' ' + argument_string + ' ' + job_list[jobname
            ]
        contents = Template(template).safe_substitute(logpath=logpath,
            respath=respath, body=job_body, jobname=jobname, memory=args.
            mem, walltime=args.walltime, pwd=pwd)
        file = open(filename, 'w')
        print >> file, contents