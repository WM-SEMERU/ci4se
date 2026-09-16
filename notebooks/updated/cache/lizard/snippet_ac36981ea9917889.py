def filter_curve(self):
    avg = np.sum(self.trial_history) / self.point_num
    standard = avg * avg * self.point_num
    predict_data = []
    tmp_model = []
    for i in range(NUM_OF_FUNCTIONS):
        var = 0
        model = curve_combination_models[i]
        for j in range(1, self.point_num + 1):
            y = self.predict_y(model, j)
            var += (y - self.trial_history[j - 1]) * (y - self.
                trial_history[j - 1])
        if var < standard:
            predict_data.append(y)
            tmp_model.append(curve_combination_models[i])
    median = np.median(predict_data)
    std = np.std(predict_data)
    for model in tmp_model:
        y = self.predict_y(model, self.target_pos)
        epsilon = self.point_num / 10 * std
        if y < median + epsilon and y > median - epsilon:
            self.effective_model.append(model)
    self.effective_model_num = len(self.effective_model)
    logger.info('List of effective model: ', self.effective_model)