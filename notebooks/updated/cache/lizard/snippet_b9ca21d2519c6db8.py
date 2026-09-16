def keep_mask(nkeep, X_train, y_train, X_test, y_test, attr_test,
    model_generator, metric, trained_model, random_state):
    X_train, X_test = to_array(X_train, X_test)
    assert X_train.shape[1] == X_test.shape[1]
    X_test_tmp = X_test.copy()
    yp_masked_test = np.zeros(y_test.shape)
    tie_breaking_noise = const_rand(X_train.shape[1], random_state) * 1e-06
    mean_vals = X_train.mean(0)
    for i in range(len(y_test)):
        if nkeep[i] < X_test.shape[1]:
            ordering = np.argsort(-attr_test[(i), :] + tie_breaking_noise)
            X_test_tmp[i, ordering[nkeep[i]:]] = mean_vals[ordering[nkeep[i]:]]
    yp_masked_test = trained_model.predict(X_test_tmp)
    return metric(y_test, yp_masked_test)