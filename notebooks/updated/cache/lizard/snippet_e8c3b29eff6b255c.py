def make_random_xml_file(fname, num_elements=200, depth=3):
    with open(fname, 'w') as f:
        f.write('<?xml version="1.0" ?>\n<random>\n')
        for dep_num, _ in enumerate(range(1, depth)):
            f.write(' <depth>\n  <content>\n')
            for num, _ in enumerate(range(1, num_elements)):
                f.write('    <stuff>data line ' + str(num) + '</stuff>\n')
            f.write('  </content>\n </depth>\n')
        f.write('</random>\n')