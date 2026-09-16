def print_pole_mean(mean_dictionary):
    print('Plon: ' + str(round(mean_dictionary['dec'], 1)) + '  Plat: ' +
        str(round(mean_dictionary['inc'], 1)))
    print('Number of directions in mean (n): ' + str(mean_dictionary['n']))
    print('Angular radius of 95% confidence (A_95): ' + str(round(
        mean_dictionary['alpha95'], 1)))
    print('Precision parameter (k) estimate: ' + str(round(mean_dictionary[
        'k'], 1)))