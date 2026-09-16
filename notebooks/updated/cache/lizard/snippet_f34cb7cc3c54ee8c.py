def process_results(output_dir, config):
    print('\nanalyzing results...\n')
    res = output_results(output_dir, config)
    if res:
        print('created: %s/results.html\n' % output_dir)
    else:
        print('results cannot be processed')