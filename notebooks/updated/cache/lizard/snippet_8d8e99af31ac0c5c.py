def read(self, line, f, data):
    assert 'hessian' not in data
    f.readline()
    N = len(data['symbols'])
    hessian = np.zeros((3 * N, 3 * N), float)
    tmp = hessian.ravel()
    counter = 0
    while True:
        line = f.readline()
        if line == ' $END\n':
            break
        line = line[5:-1]
        for j in range(len(line) // 15):
            tmp[counter] = float(line[j * 15:(j + 1) * 15])
            counter += 1
    data['hessian'] = hessian