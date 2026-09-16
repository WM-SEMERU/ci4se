def pick_target_decoy(tfeature, dfeature):
    tscore, dscore = get_score(tfeature), get_score(dfeature)
    if tscore == dscore:
        return False
    elif False in [tscore, dscore]:
        return [v for k, v in {tscore: tfeature, dscore: dfeature}.items() if
            k is not False][0]
    elif tscore > dscore:
        return tfeature
    elif tscore < dscore:
        return dfeature
    else:
        print(
            'WARNING, target score {} and decoy score {} could not be compared'
            .format(tscore, dscore))
        return False