def lis_to_bio_map(folder):
    logger.info('Opening legislator csv for lis_dct creation')
    lis_dic = {}
    leg_path = '{0}/legislators.csv'.format(folder)
    logger.info(leg_path)
    with open(leg_path, 'r') as csvfile:
        leg_reader = csv.reader(csvfile)
        for row in leg_reader:
            if row[22]:
                lis_dic[row[22]] = row[19]
    return lis_dic