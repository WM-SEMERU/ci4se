def write_single_file(args, base_dir, crawler):
    if args['urls'] and args['html']:
        domain = utils.get_domain(args['urls'][0])
        if not args['quiet']:
            print('Storing html files in {0}/'.format(domain))
        utils.mkdir_and_cd(domain)
    infilenames = []
    for query in args['query']:
        if query in args['files']:
            infilenames.append(query)
        elif query.strip('/') in args['urls']:
            if args['crawl'] or args['crawl_all']:
                infilenames += crawler.crawl_links(query)
            else:
                raw_resp = utils.get_raw_resp(query)
                if raw_resp is None:
                    return False
                prev_part_num = utils.get_num_part_files()
                utils.write_part_file(args, query, raw_resp)
                curr_part_num = prev_part_num + 1
                infilenames += utils.get_part_filenames(curr_part_num,
                    prev_part_num)
    if args['html']:
        os.chdir(base_dir)
    elif infilenames:
        if args['out']:
            outfilename = args['out'][0]
        else:
            outfilename = utils.get_single_outfilename(args)
        if outfilename:
            write_files(args, infilenames, outfilename)
    else:
        utils.remove_part_files()
    return True