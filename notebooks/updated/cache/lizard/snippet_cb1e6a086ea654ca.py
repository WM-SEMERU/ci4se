def learningCurve(expPath, suite):
    print('\nLEARNING CURVE ================', expPath, '====================='
        )
    try:
        headers = ['testerror', 'totalCorrect', 'elapsedTime', 'entropy']
        result = suite.get_value(expPath, 0, headers, 'all')
        info = []
        for i, v in enumerate(zip(result['testerror'], result[
            'totalCorrect'], result['elapsedTime'], result['entropy'])):
            info.append([i, v[0], v[1], int(v[2]), v[3]])
        headers.insert(0, 'iteration')
        print(tabulate(info, headers=headers, tablefmt='grid'))
    except:
        print("Couldn't load experiment", expPath)