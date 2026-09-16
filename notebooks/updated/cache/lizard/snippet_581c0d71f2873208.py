def summarise_file_as_html(fname):
    txt = '<H1>' + fname + '</H1>'
    num_lines = 0
    print('Reading OpenCyc file - ', fname)
    with open(ip_folder + os.sep + fname, 'r') as f:
        txt += '<PRE>'
        for line in f:
            if line.strip() != '':
                num_lines += 1
                if num_lines < 80:
                    txt += str(num_lines) + ': ' + escape_html(line) + ''
        txt += '</PRE>'
        txt += 'Total lines = ' + str(num_lines) + '<BR><BR>'
    return txt