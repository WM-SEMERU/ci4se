def _log_rate(output_f, d, message=None):
    if d[2] <= 0:
        if message is None:
            message = d[4]
        d[6].append(int(d[3] / (time() - d[1])))
        rate = sum(d[6]) / len(d[6])
        output_f(message + ': ' + str(rate) + '/s ' + str(d[0] / 1000) + 'K ')
        d[1] = time()
        if d[5]:
            target_rate = rate * d[5]
            d[3] = int((target_rate + d[3]) / 2)
        d[2] = d[3]
    d[0] += 1
    d[2] -= 1