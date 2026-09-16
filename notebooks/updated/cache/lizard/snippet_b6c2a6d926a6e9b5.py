def cost_loss(y_true, y_pred, cost_mat):
    y_true = column_or_1d(y_true)
    y_true = (y_true == 1).astype(np.float)
    y_pred = column_or_1d(y_pred)
    y_pred = (y_pred == 1).astype(np.float)
    cost = y_true * ((1 - y_pred) * cost_mat[:, (1)] + y_pred * cost_mat[:,
        (2)])
    cost += (1 - y_true) * (y_pred * cost_mat[:, (0)] + (1 - y_pred) *
        cost_mat[:, (3)])
    return np.sum(cost)