def backprop(self, input_data, targets, cache=None):
    df_input = gpuarray.zeros_like(input_data)
    if cache is None:
        cache = self.n_tasks * [None]
    gradients = []
    for targets_task, cache_task, task, task_weight in izip(targets, cache,
        self.tasks, self.task_weights):
        gradients_task, df_input_task = task.backprop(input_data,
            targets_task, cache_task)
        df_input = df_input.mul_add(1.0, df_input_task, task_weight)
        gradients.extend(gradients_task)
    return gradients, df_input