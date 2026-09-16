def min_sequence_length(self, dataset_split):
    return {problem.DatasetSplit.TRAIN: 8, problem.DatasetSplit.EVAL: 65,
        problem.DatasetSplit.TEST: 65}[dataset_split]