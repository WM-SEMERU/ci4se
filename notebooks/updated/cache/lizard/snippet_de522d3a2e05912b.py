def city_nums():
    city_nums = {}
    first_row = 1
    num = 0
    fname = pkg_resources.resource_filename(__name__,
        'resources/Distance_Matrix.csv')
    with open(fname, 'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if first_row == 1:
                first_row = 0
            else:
                city_nums[row[0]] = num
                num = num + 1
    return city_nums