def cdfout(data, file):
    f = open(file, 'w')
    data.sort()
    for j in range(len(data)):
        y = old_div(float(j), float(len(data)))
        out = str(data[j]) + ' ' + str(y) + '\n'
        f.write(out)
    f.close()