def ND_all_available():
    ND_all_available = []
    for i in range(len(pipedb['NDinch'])):
        if pipedb.iloc[i, 4] == 1:
            ND_all_available.append(pipedb['NDinch'][i])
    return ND_all_available * u.inch